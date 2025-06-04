import wikipedia
from pydantic import BaseModel, ValidationError
from typing import Optional
import re

# Define the Pydantic schema for the institution details
class InstitutionInfo(BaseModel):
    name: str
    founder: Optional[str]
    founded: Optional[str]
    branches: Optional[str]
    employees: Optional[str]
    summary: Optional[str]

def extract_institution_details(institution_name: str) -> Optional[InstitutionInfo]:
    try:
        # Fetch the Wikipedia page content
        page = wikipedia.page(institution_name)
        content = page.content

        # Initialize fields
        founder = None
        founded = None
        branches = None
        employees = None

        # Extract founder
        founder_match = re.search(r'(?i)founder[s]?:\s*(.*)', content)
        if founder_match:
            founder = founder_match.group(1).split('\n')[0].strip()

        # Extract founded date
        founded_match = re.search(r'(?i)founde[dn]:\s*(.*)', content)
        if founded_match:
            founded = founded_match.group(1).split('\n')[0].strip()

        # Extract branches
        branches_match = re.search(r'(?i)branches:\s*(.*)', content)
        if branches_match:
            branches = branches_match.group(1).split('\n')[0].strip()

        # Extract number of employees
        employees_match = re.search(r'(?i)employee[s]?:\s*(.*)', content)
        if employees_match:
            employees = employees_match.group(1).split('\n')[0].strip()

        # Generate a brief 4-line summary
        summary_sentences = wikipedia.summary(institution_name, sentences=4)

        # Create the InstitutionInfo object
        institution_info = InstitutionInfo(
            name=institution_name,
            founder=founder,
            founded=founded,
            branches=branches,
            employees=employees,
            summary=summary_sentences
        )
        return institution_info

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
    except wikipedia.exceptions.PageError:
        print("Page not found.")
    except ValidationError as ve:
        print(f"Validation error: {ve}")
    return None

# Example usage
if __name__ == "__main__":
    institution_name = input("Enter the name of the institution: ")
    info = extract_institution_details(institution_name)
    if info:
        print("\nExtracted Institution Details:")
        print(info.model_dump_json(indent=4))
