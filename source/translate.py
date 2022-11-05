from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient

endpoint = "https://vegito54.cognitiveservices.azure.com/"
credential = AzureKeyCredential("8b94267865d445d599114d250e9d5977")
source_container_sas_url_en = "https://mypjct.blob.core.windows.net/data1?sp=rl&st=2022-10-25T19:54:23Z&se=2022-10-26T03:54:23Z&spr=https&sv=2021-06-08&sr=c&sig=1znyzKuz%2FbjMTqS8BOeSe3mDzPLjMqamZCju66FRp1A%3D"
target_container_sas_url_es = "https://mypjct.blob.core.windows.net/translated?sp=cwl&st=2022-10-25T19:58:20Z&se=2022-10-26T03:58:20Z&spr=https&sv=2021-06-08&sr=c&sig=FhXzys3eOyp5w0p0dO6A%2FnpgshcMY4%2FdVVvLxzXFhYM%3D"

document_translation_client = DocumentTranslationClient(endpoint, credential)

poller = document_translation_client.begin_translation(source_container_sas_url_en, target_container_sas_url_es, "es")

result = poller.result()

print(f"Status: {poller.status()}")
print(f"Created on: {poller.details.created_on}")
print(f"Last updated on: {poller.details.last_updated_on}")
print(f"Total number of translations on documents: {poller.details.documents_total_count}")

print("\nOf total documents...")
print(f"{poller.details.documents_failed_count} failed")
print(f"{poller.details.documents_succeeded_count} succeeded")

for document in result:
    print(f"Document ID: {document.id}")
    print(f"Document status: {document.status}")
    if document.status == "Succeeded":
        print(f"Source document location: {document.source_document_url}")
        print(f"Translated document location: {document.translated_document_url}")
        print(f"Translated to language: {document.translated_to}\n")
    else:
        print(f"Error Code: {document.error.code}, Message: {document.error.message}\n")