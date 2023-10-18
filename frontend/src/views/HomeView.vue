<template>
  <div id="home">
    <section id="hero">
      <h1 class="tagline">Äriühingud</h1>
    </section>
    <section class="search-wrapper">
      <input
        type="text"
        name="legal-entity-search-term"
        id="search-input"
        class="search-input"
        placeholder="Otsing"
        v-model="searchTerm"
        @input="search"
      />
      <p class="tip search-input-tip">
        Nimi, registrikood, osaniku nimi või isikukood
      </p>
    </section>
    <section class="legal-entity-search-results" v-if="searchTerm">
      <div
        class="legal-entity-search-results__wrapper"
        v-if="results.length > 0 && !loading"
      >
        <table class="legal-entity-search-results__table">
          <thead>
            <tr class="legal-entity-search-results__table-row">
              <th class="legal-entity-search-results__table-cell">Nimi</th>
              <th class="legal-entity-search-results__table-cell">
                Registrikood
              </th>
              <th class="legal-entity-search-results__table-cell">
                Osakapital
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="legalEntity in results"
              :key="legalEntity.id"
              @click.stop="router.push(`/legal-entity/${legalEntity.id}`)"
              class="legal-entity-search-result legal-entity-search-results__table-row"
            >
              <td class="legal-entity-search-results__table-cell">
                {{ legalEntity.name }}
              </td>
              <td class="legal-entity-search-results__table-cell">
                {{ legalEntity.registryCode }}
              </td>
              <td class="legal-entity-search-results__table-cell">
                {{ legalEntity.created }}
              </td>
            </tr>
          </tbody>
        </table>
        <p class="tip results-search-tip">
          Tulemuste arv: {{ results.length }}
        </p>
      </div>
      <div v-else-if="!loading && results.length == 0">
        <p class="search-no-results">Tulemusi ei leitud</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { LegalEntity } from "@/models/legal-entity";
import router from "@/router";

const searchTerm = ref<null | string>(null);
const loading = ref<boolean>(false);
const results = ref<LegalEntity[]>([]);

const search = () => {
  loading.value = true;
  if (searchTerm.value && searchTerm.value.length >= 3) {
    fetch(`http://localhost:8000/legal-entity/search?term=${searchTerm.value}`)
      .then((response) => response.json())
      .then((data) => {
        results.value = data;
        loading.value = false;
      });
  }
};
</script>

<style lang="scss" scoped>
#hero {
  padding: 96px 32px;
  text-align: center;
}

.tagline {
  font-size: 48px;
}

.search-input {
  border: 0;
  border-bottom: 1px solid rgba(60, 60, 60, 0.12);
  font-size: 32px;
  padding: 10px;
  box-sizing: border-box;

  &:focus {
    outline-width: 0;
  }
}

.search-wrapper {
  padding: 32px 0;
  text-align: center;
}

.tip {
  padding: 5px;
  margin-top: 5px;
  font-size: 0.75rem;
  color: dimgray;
}

.legal-entity-search-results {
  width: 100%;
  display: inline-flex;
  justify-content: center;
}

table,
thead {
  border: solid 1px rgba(60, 60, 60, 0.12);
  border-collapse: collapse;
  min-width: 500px;
}

thead {
  background: #3185fc;
}

.legal-entity-search-result:hover {
  cursor: pointer;
}

td,
th {
  padding: 5px;
}

.search-no-results {
  font-size: 1.6rem;
}
</style>
