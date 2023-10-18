<template>
  <div id="legal-entity">
    <div class="legal-entity-content" v-if="legalEntity">
      <h1>{{ legalEntity.name }}</h1>
      <table>
        <tbody>
          <tr>
            <td class="field-description">Registrikood</td>
            <td class="field-content">{{ legalEntity.registryCode }}</td>
          </tr>
          <tr>
            <td class="field-description">Registreeritud</td>
            <td class="field-content">
              {{ legalEntity.created }}
            </td>
          </tr>
          <tr>
            <td class="field-description">Osakapital</td>
            <td class="field-content">
              {{ divideThousands(legalEntity.capital) }}
              €
            </td>
          </tr>
        </tbody>
      </table>
      <h2>Osanikud</h2>
      <table class="shareholders-table">
        <thead>
          <tr>
            <th></th>
            <th class="shareholders-table-header__cell">Nimi</th>
            <th class="shareholders-table-header__cell">Kood</th>
            <th class="shareholders-table-heade__cell">Asutaja</th>
            <th class="shareholders-table-header__cell">Osamaks</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="shareholder in legalEntity.shareholders"
            :key="shareholder.code"
          >
            <td>
              <font-awesome-icon
                :icon="
                  shareholder.type === ShareholderType.LegalEntity
                    ? 'users'
                    : 'user'
                "
              ></font-awesome-icon>
            </td>
            <td class="shareholders-table__cell">{{ shareholder.name }}</td>
            <td class="shareholders-table__cell">{{ shareholder.code }}</td>
            <td class="shareholders-table__cell">
              {{ shareholder.founder ? "Jah" : "Ei" }}
            </td>
            <td class="shareholders-table__cell">
              {{ divideThousands(shareholder.share) }} €
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import router from "@/router";
import { ref } from "vue";
import { DetailedLegalEntity } from "@/models/detailed-legal-entity";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { ShareholderType } from "@/models/shareholder-type";
import { divideThousands } from "@/utils/number-utils";

const id = router.currentRoute.value.params.id;
const legalEntity = ref<DetailedLegalEntity | null>(null);
fetch(`http://localhost:8000/legal-entity/${id}`)
  .then((response) => response.json())
  .then((data) => (legalEntity.value = data));
</script>

<style scoped>
.field-description {
  width: 150px;
}

table {
  min-width: 400px;
}

.shareholders-table__cell,
.shareholders-table-header__cell {
  min-width: 80px;
  width: 130px;
  padding: 0 5px;
}
</style>
