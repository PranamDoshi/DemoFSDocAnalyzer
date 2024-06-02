export enum BackendDocumentType {
  // TenK = "10-K",
  // TenQ = "10-Q",
  FS = "Financial Statement"
}

export interface BackendDocument {
  created_at: string;
  id: string;
  updated_at: string;
  metadata_map: BackendMetadataMap;
  url: string;
}

export interface BackendMetadataMap {
  // sec_document: BackendBseDocument;
  bse_document: BackendBseDocument;
}

export interface BackendBseDocument {
  company_name: string;
  company_ticker: string;
  doc_type: BackendDocumentType;
  year: string;
  // quarter: number;
}
