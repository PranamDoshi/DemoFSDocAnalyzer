import { MAX_NUMBER_OF_SELECTED_DOCUMENTS } from "~/hooks/useDocumentSelector";
import { BackendDocument, BackendDocumentType } from "~/types/backend/document";
import { BseDocument, DocumentType } from "~/types/document";
import { documentColors } from "~/utils/colors";
import _ from "lodash";

export const fromBackendDocumentToFrontend = (
  backendDocuments: BackendDocument[]
) => {
  console.log(backendDocuments.length)
  // sort by created_at so that de-dupe filter later keeps oldest duplicate docs
  backendDocuments = _.sortBy(backendDocuments, 'created_at');
  let frontendDocs: BseDocument[] = backendDocuments
  // .filter((backendDoc) => 'bse_document' in backendDoc.metadata_map)
  .map((backendDoc, index) => {
    // const backendDocType = backendDoc.metadata_map.bse_document.doc_type;
    // const frontendDocType = DocumentType.FS
      // backendDocType === BackendDocumentType.FS
      //   ? DocumentType.TenK
      //   : DocumentType.TenQ;

    // we have 10 colors for 10 documents
    const colorIndex = index < 10 ? index : 0;
    return {
      id: backendDoc.id,
      url: backendDoc.url,
      ticker: backendDoc.metadata_map.bse_document.company_ticker,
      fullName: backendDoc.metadata_map.bse_document.company_name,
      year: backendDoc.metadata_map.bse_document.year,
      docType: DocumentType.FS,
      color: documentColors[colorIndex],
      // quarter: backendDoc.metadata_map.bse_document.quarter || "",
    } as BseDocument;
  });
  // de-dupe hotfix
  // const getDocDeDupeKey = (doc: BseDocument) => `${doc.ticker}-${doc.year}-${doc.quarter || ''}`;
  const getDocDeDupeKey = (doc: BseDocument) => `${doc.ticker}-${doc.year}`;
  frontendDocs = _.chain(frontendDocs).sortBy(getDocDeDupeKey).sortedUniqBy(getDocDeDupeKey).value();
  console.log(frontendDocs.length)

  return frontendDocs;
};
