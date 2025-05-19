import json
from datetime import date

def create_zenodo_metadata():
    """Prompts the user for metadata and creates a METADATA.json file."""

    metadata = {}

    # Required fields
    metadata['upload_type'] = 'dataset'
    metadata['publication_date'] = date.today().strftime('%Y-%m-%d')
    metadata['title'] = input("Enter the title of your data set: ")

    creators = []
    while True:
        creator = {}
        creator['name'] = input("Enter creator name (or type 'done' if finished): ")
        if creator['name'].lower() == 'done':
            break
        creator['orcid'] = input("Enter ORCID for this creator (optional, leave blank if none): ") or None
        creator['affiliation'] = input("Enter affiliation for this creator (optional, leave blank if none): ") or None
        creators.append(creator)
    metadata['creators'] = creators

    metadata['description'] = input("Enter a detailed description of your data set: ")

    while True:
        access_right = input("Enter access right (open, restricted, embargoed, closed): ").lower()
        if access_right in ['open', 'restricted', 'embargoed', 'closed']:
            metadata['access_right'] = access_right
            if access_right == 'embargoed':
                metadata['embargo_date'] = input("Enter embargo date (YYYY-MM-DD): ")
            elif access_right == 'open':
                metadata['license'] = input("Enter license (e.g., CC-BY-4.0 or URL): ") or None
            break
        else:
            print("Invalid access right. Please choose from: open, restricted, embargoed, closed.")

    # Recommended fields
    keywords = input("Enter keywords separated by commas (optional): ")
    metadata['keywords'] = [k.strip() for k in keywords.split(',')] if keywords else []

    related_identifiers = []
    while True:
        related = {}
        relation = input("Enter relation to another identifier (e.g., isSupplementTo, isCitedBy, or type 'done' if finished): ").lower()
        if relation == 'done':
            break
        related['relation'] = relation
        related['identifier'] = input("Enter the identifier (e.g., DOI): ")
        related['scheme'] = input("Enter the identifier scheme (e.g., doi, url, handle): ")
        related_identifiers.append(related)
    metadata['related_identifiers'] = related_identifiers

    metadata['version'] = input("Enter the version of the data set (optional): ") or None

    communities = []
    while True:
        community_id = input("Enter Zenodo community ID (or type 'done' if finished): ")
        if community_id.lower() == 'done':
            break
        communities.append({"id": community_id})
    metadata['communities'] = communities

    references = []
    while True:
        reference = input("Enter a reference (or type 'done' if finished): ")
        if reference.lower() == 'done':
            break
        references.append({"reference": reference})
    metadata['references'] = references

    metadata['notes'] = input("Enter any additional notes (optional): ") or None

    # Write the metadata to a JSON file
    with open('METADATA.json', 'w') as f:
        json.dump(metadata, f, indent=2)

    print("METADATA.json file created successfully!")

if __name__ == "__main__":
    create_zenodo_metadata()
