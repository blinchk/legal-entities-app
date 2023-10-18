import LegalEntityCreateShareholder from "@/models/dto/legal-entity-create-shareholder";

export default interface LegalEntityCreate {
  name: string | null;
  registryCode: string | null;
  created: string;
  capital: number | null;
  shareholders: LegalEntityCreateShareholder[];
}
