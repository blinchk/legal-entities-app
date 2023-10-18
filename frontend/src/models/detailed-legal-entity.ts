import { LegalEntity } from "@/models/legal-entity";
import Shareholder from "@/models/shareholder";

export interface DetailedLegalEntity extends LegalEntity {
  shareholders: Shareholder[];
}
