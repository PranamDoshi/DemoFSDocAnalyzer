import { DocumentColorEnum } from "~/utils/colors";

export enum DocumentType {
  // TenK = "Form 10K",
  // TenQ = "Form 10Q",
  FS = "FinancialStatement"
}

export type Ticker = {
  ticker: string;
  fullName: string;
};

// export interface BseDocument extends Ticker {
//   id: string;
//   url: string;
//   year: string;
//   docType: DocumentType;
//   quarter?: string;
//   color: DocumentColorEnum;
// }

export interface BseDocument extends Ticker {
  id: string;
  url: string;
  year: string;
  docType: DocumentType;
  // quarter?: string;
  // color: DocumentColorEnum;
}
