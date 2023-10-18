import { ShareholderType } from "@/models/shareholder-type";

export default interface Shareholder {
  id: number;
  type: ShareholderType;
  name: string;
  code: string;
  founder: boolean;
  share: number;
}
