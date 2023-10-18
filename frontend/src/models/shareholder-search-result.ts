import { ShareholderType } from "@/models/shareholder-type";

export default interface ShareholderSearchResult {
  id: number;
  type: ShareholderType;
  name: string;
  code: string;
}
