"""
NSE API:
curl 'https://www.nseindia.com/api/annual-reports?index=equities&symbol=TCS' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: defaultLang=en; bm_sz=8559D568F63B079A2589122BFF58781F~YAAQdIMsMYuFGaSPAQAAWTnTzxdx53E9u1Iu2sp1vkEetvI52CbHog3N1J9AFU/Zn5GQskZeRDxCnIvi1VaO3Y5f2njIFy+/34KfwxmFIPi8b4ZUza0hrtJv72udUrQA40gRo2IJA1I40pzzall63HAikwnud3Q6lk9QVSc/4fYOeXabJTTPvFzPnKbB6SiKbB3zGfjRy2XAGmLzI7Gph8WOKuzaUsRlHsVFd5wSfJRtTuAIn8YT6gTpgPS6LdWJpQwEDYcM1ZSNCho/T9RJToSu1IIBHNZ7GJv6TdAVuVIu0ZNzPl7nq4wfD5jaFuSYsIM5PNP75QLYulI3XhI2JghMPSi2QzEXTtVBQZieSdEe3V5aq93zxCftmPjJV/TmTrcvi10BuJ6gYc/dZIeT7rzx9Jdwub1rSX+Y2eOs6FwtTuplkpuIXRk7t+t85wGuLSNiVMc6dxUHduCbQQ==~3486515~4408899; nsit=d7I-Mq0yoifs2q8LKoo0m0qf; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxNzE4MDc1NCwiZXhwIjoxNzE3MTg3OTU0fQ.sv0kDL0nsr_A1yBLVyU5icgv_weCTAV9f_Yf2ScOpEY; AKA_A2=A; bm_mi=2AE4C5DFCDB24B3101CCC1D0C029FFFB~YAAQdIMsMfJLGqSPAQAAi+zyzxeNSWSuI+TX5dnDILradoWINsBt2j3i+wcZ7u290qx0C4y5AHJ9snrrXRWj5U5I+BsecONniWcof7Bu0he69+PDi19ZuUNMtm/+sm7n8z49c9hkMt0YsMNpu8hyAgvjMjnxJi6RTQZZYiJqAjtsyb/qnSgKMJ1/rnTp0NpFPbheKIKdi6SV1ORIDlqA7N6ATiXolQc5LC3ozANkJ4jHmVoO0fBkY+8mobhKINQvfC7tSdm4wIyTajkywkZwgywtbmPAhCA7DyuJaezMeYouRbCrZftNVzuqAXK3JiVqkO1h3VQbotIhDuGssl4Ed9WspaMzX5oj0FYKQttnxbhA3XGQXIOpX6yUcKiPX4VWjdA=~1; ak_bmsc=18E1F8ED02DCDEE18BF28F0130306AFF~000000000000000000000000000000~YAAQdIMsMU1MGqSPAQAATPPyzxerh0G5CRo+Xhod0YEB64zzo3CR3T9F9CGz3hDW+vOPNlr6ykUp+Z4JKHCoxHkkRkFt2yrfeueHoQKYCit06QZVgo+HuVkh80AK0v8meUFYf5U2Xvep8ti0nu3YsaJpRUTj9BwwJNTRg72Fzt2bmPWAB7ZhsKLOS+hvRlNPmqpmegOAZ4+K6qdCHCVXXphuOFYWGEPWl2njrsLTCmms4OI4GWvzIQQYRkcgV7RoznNvxmW8qecKHbInZBGrBibj6JyMHuCw69Q1zOgqV7GrPbXQ98zOIpSqzVIiEWX+q0gzvVDbAcDc1aHtkCXYzheuHjcVNeD5GsFFowqd/XBZ+mMuMDzcttUwFLWdchWDlVC/44cjtGR2gLFB4A+tH53jwFtbtX9PCdtNqz4LLAMBBmktkjcrSn3vleaOgZkemaQ04wcRoHr8raa+dLIdgPZyJK2PKYvO7xseu7TmK/0c5U7hZ7JBJ34ReZbeD6g022gKSJTpFmxcgf94PR2fK2p4Tie89hgObAIyYYieyHLGUg==; bm_sv=806A6D4993E14F750230C77E5A925C3D~YAAQdIMsMYFMGqSPAQAAFgDzzxes1jOXGENOUHGWVpcKmatt1ieE1TPJlOF0duKk+Y53HAtinP8EvxwzCskzB/Hj9KrbYY+QXF4AzRBb1gYMY6ZhppziosuALh4bjRaEGOePQoY/wQ6P/ZuD8dGFsu1XESNkCZ9iAYuuBHLEL7sPmopLpZRTdbTg2Z1Wy0o3TUhjFn4TpMcXWOHZkLB9q9VwMbqZkyzBP9g799Oat+VfqTz87I8BUmdfSBT4OR3JfbMp~1; _abck=25409260B14F72F41AF785E0041B2B4D~0~YAAQdIMsMYNMGqSPAQAAfgDzzwv9MkWvk90ku3DZ9pbLYL/b7FsBE6F6yxPCN5eG/SWBOibAtx4/Sf5iT28KeOYAbrdTg7260SRppxcftJphH/9uywJtMQOdqcwiWvmpu4rBsDhl0Jrr4yVyuMPLgzdb64nlXpjrRNQUHyF2PEcWNDlTvhFqLoSKOx4YN8D4yiB78uDUe+setkncMecNvDQ09qvmx6L/UnrubaAP6UZ0N/a4d9T000DWiFCm5sdzh9ILUvma8FSLlNxcscrThNXEJ/FpdL3iCwYgq5tYBLQAs0s9JJcc3DFJt8CXFnMKhGWwp2inOVr6qjI53i77XDqp46hWVg2DkfZ3JMzXaaNBkwsIrVTdQ9xIyAjwS3iX~-1~-1~-1' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.nseindia.com/companies-listing/corporate-filings-annual-reports' \
  -H 'sec-ch-ua: "Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
"""
from pathlib import Path
from fire import Fire
from tqdm import tqdm
import asyncio, json
from pytickersymbols import PyTickerSymbols
from file_utils import get_available_filings, Filing
from stock_utils import get_stocks_by_symbol, Stock
from fastapi.encoders import jsonable_encoder
from app.models.db import Document
from app.schema import (
    BSEDocumentMetadata,
    DocumentMetadataMap,
    DocumentMetadataKeysEnum,
    Document,
)
from app.db.session import SessionLocal
from app.api import crud

# BSE_Documents_by_Company = {
#     "WIPRO LTD.": [
#         {
#             "company_ticker": "WIPRO",
#             "year": "2023",
#             "pdf_url": "https://www.bseindia.com/xml-data/corpfiling/AttachHis//ea6ff555-0162-4acf-98b2-0ef7a7a26699.pdf"
#         },
#         {
#             "company_ticker": "WIPRO",
#             "year": "2022",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/507685/73311507685.pdf"
#         },
#         {
#             "company_ticker": "WIPRO",
#             "year": "2021",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/507685/68597507685.pdf"
#         }
#     ],
#     "TECH MAHINDRA LTD.": [
#         {
#             "company_ticker": "TECHM",
#             "year": "2023",
#             "pdf_url": "https://www.bseindia.com/xml-data/corpfiling/AttachHis//80910fd6-6181-45f3-945b-5cb743f26965.pdf"
#         },
#         # {
#         #     "company_ticker": "TECHM",
#         #     "year": "2022",
#         #     "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/532755/73354532755.pdf"
#         # },
#         {
#             "company_ticker": "TECHM",
#             "year": "2021",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/532755/68770532755.pdf"
#         },
#         {
#             "company_ticker": "TECHM",
#             "year": "2020",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/532755/5327550320.pdf"
#         }
#     ],
#     "INFOSYS LTD.": [
#         {
#             "company_ticker": "INFY",
#             "year": "2023",
#             "pdf_url": "https://www.bseindia.com/xml-data/corpfiling/AttachHis//3ba3c011-0411-49ba-a250-f746a5b9d940.pdf"
#         },
#         {
#             "company_ticker": "INFY",
#             "year": "2022",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/500209/73015500209_29_06_22.pdf"
#         },
#         {
#             "company_ticker": "INFY",
#             "year": "2021",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/500209/68476500209_09_06_21.pdf"
#         }
#     ],
#     "TATA CONSULTANCY SERVICES LTD.": [
#         {
#             "company_ticker": "TCS",
#             "year": "2023",
#             "pdf_url": "https://www.bseindia.com/xml-data/corpfiling/AttachHis//3837c1b7-9308-436d-9636-1d6856edf74e.pdf"
#         },
#         {
#             "company_ticker": "TCS",
#             "year": "2022",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/532540/72996532540_17_06_22.pdf"
#         },
#         {
#             "company_ticker": "TCS",
#             "year": "2021",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/532540/68468532540_25_05_21.pdf"
#         }
#     ],
#     "HCL TECHNOLOGIES LTD.": [
#         {
#             "company_ticker": "HCLTECH",
#             "year": "2023",
#             "pdf_url": "https://www.bseindia.com/xml-data/corpfiling/AttachHis//e7b8d757-92a5-423c-a450-3d4fb68e6b6e.pdf"
#         },
#         {
#             "company_ticker": "HCLTECH",
#             "year": "2022",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/532281/73863532281.pdf"
#         },
#         {
#             "company_ticker": "HCLTECH",
#             "year": "2021",
#             "pdf_url": "https://www.bseindia.com/bseplus/AnnualReport/532281/69289532281.pdf"
#         }
#     ]
# }
with open('/workspaces/sec-insights/backend/scripts/BSE_Documents_by_Company_Dropbox_URLs.json', 'r') as f:
    BSE_Documents_by_Company = json.load(f)

async def upsert_document(pdf_url: str, filing_year: str, company_name: str, company_ticker: str):
    """ 
    Constructs the document in system.
    """
    bse_doc_metadata = BSEDocumentMetadata(
        company_name=company_name,
        company_ticker=company_ticker,
        year=filing_year
    )
    metadata_map: DocumentMetadataMap = {
        DocumentMetadataKeysEnum.BSE_DOCUMENT: jsonable_encoder(
            bse_doc_metadata.dict(exclude_none=True)
        )
    }
    doc = Document(url=pdf_url, metadata_map=metadata_map)
    async with SessionLocal() as db:
        await crud.upsert_document_by_url(db, doc)

async def main_upsert_documents():
    """
    Upserts BSE documents into the database using the config.
    """
    for company_name, filings in BSE_Documents_by_Company.items():
        for filing_details in filings:
            await upsert_document(filing_details['pdf_url'], filing_details['year'], company_name, filing_details['company_ticker'])

if __name__ == "__main__":
    asyncio.run(main_upsert_documents())
