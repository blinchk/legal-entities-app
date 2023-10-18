import ShareholderSearchResult from "@/models/shareholder-search-result";

export default interface LegalEntityCreateShareholder
  extends ShareholderSearchResult {
  share: number;
}
