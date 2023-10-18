<template>
  <div id="create-new-legal-entity">
    <h1>Osaühingu asutamine</h1>
    <form>
      <div class="legal-entity-form-column">
        <div class="legal-entity-form-group">
          <label for="legal-entity-name" class="legal-entity-form-field__label"
            >Nimi</label
          >
          <input
            type="text"
            name="legal-entity-name"
            id="legal-entity-name"
            v-model="legalEntity.name"
            class="legal-entity-form-field__input"
          />
          <pre> OÜ</pre>
        </div>
        <div class="legal-entity-form-group">
          <label for="legal-entity-code" class="legal-entity-form-field__label"
            >Registrikood</label
          >
          <input
            type="text"
            name="legal-entity-code"
            id="legal-entity-code"
            v-model="legalEntity.registryCode"
            class="legal-entity-form-field__input"
          />
        </div>
        <div class="legal-entity-form-group">
          <label
            for="legal-entity-created"
            class="legal-entity-form-field__label"
            >Asutamiskuupäev</label
          >
          <input
            type="date"
            name="legal-entity-created"
            id="legal-entity-created"
            v-model="legalEntity.created"
            :max="todayDate()"
            class="legal-entity-form-field__input"
          />
        </div>
      </div>
      <div class="legal-entity-form-group">
        <label for="legal-entity-share" class="legal-entity-form-field__label"
          >Osakapital</label
        >
        <div id="legal-entity-share">{{ currentCapital }} €</div>
      </div>
    </form>
    <h2>Osanikud</h2>
    <table class="shareholders-table">
      <thead>
        <tr>
          <th></th>
          <th class="shareholders-table-header__cell">Nimi</th>
          <th class="shareholders-table-header__cell">Kood</th>
          <th class="shareholders-table-header__cell">Asutaja</th>
          <th class="shareholders-table-header__cell">Osamaks</th>
          <th class="shareholders-table-header__cell"></th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(shareholder, index) in shareholders"
          :key="shareholder.code"
        >
          <td class="shareholder-type-cell">
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
          <td class="shareholders-table__cell">Jah</td>
          <td class="shareholders-table__cell">
            <div class="shareholder-share__input-group">
              <input
                type="number"
                name="shareholder-share"
                class="shareholder-share__input"
                min="1"
                :id="`shareholder-${shareholder.code}-share`"
                v-model="shareholders[index].share"
              />
              <pre> €</pre>
            </div>
          </td>
          <td class="shareholder-table__cell">
            <a
              class="shareholder-action shareholder-action__delete btn"
              @click.stop="removeShareholder(index)"
            >
              <font-awesome-icon
                icon="close"
                size="lg"
                class="shareholder-action-icon"
              ></font-awesome-icon>
              <strong>Kustuta</strong>
            </a>
          </td>
        </tr>
        <tr>
          <td></td>
          <td>
            <input
              type="text"
              class="shareholder-search"
              name="shareholder-search"
              id="shareholder-search"
              placeholder="Isiku nimi"
              v-model="searchTerm"
              @input="search"
            />
            <div
              class="shareholder-autocomplete"
              v-if="results.length > 0 && !loading"
            >
              <div class="shareholder-autocomplete-results">
                <li
                  class="shareholder-autocomplete-results__result"
                  v-for="result in results"
                  :key="result.id"
                  @click.stop="addShareholder(result)"
                >
                  {{ result.name }} ({{ result.code }})
                </li>
              </div>
            </div>
          </td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
    <div class="legal-entity-actions">
      <a class="btn create-new-entity-btn" v-if="valid" @click.stop="create"
        >Luua</a
      >
      <a class="btn create-new-entity-btn btn-inactive" v-else>Luua</a>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { computed, ref, toRaw } from "vue";
import LegalEntityCreate from "@/models/dto/legal-entity-create";
import { generateRegistryCode } from "@/clients/legal-entity-client";
import { todayDate } from "@/utils/date-utils";
import ShareholderSearchResult from "@/models/shareholder-search-result";
import LegalEntityCreateShareholder from "@/models/dto/legal-entity-create-shareholder";
import { ShareholderType } from "@/models/shareholder-type";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import router from "@/router";

const legalEntity = ref<LegalEntityCreate>({
  name: null,
  registryCode: null,
  created: todayDate(),
  capital: null,
  shareholders: [],
});

const shareholders = ref<LegalEntityCreateShareholder[]>([]);

const searchTerm = ref<string | null>(null);
const results = ref<ShareholderSearchResult[]>([]);
const loading = ref<boolean>(false);

generateRegistryCode().then((registryCode) => {
  legalEntity.value.registryCode = registryCode;
});

const search = () => {
  results.value = [];
  if (searchTerm.value && searchTerm.value.length >= 3) {
    loading.value = true;
    fetch(
      `http://localhost:8000/legal-entity/new/shareholder/search?term=${searchTerm.value}`
    )
      .then((response) => response.json())
      .then((data) => {
        results.value = data;
        loading.value = false;
      });
  }
};

const addShareholder = (shareholder: ShareholderSearchResult) => {
  shareholders.value.push({
    ...toRaw(shareholder),
    share: 1,
  });
  results.value = [];
  searchTerm.value = null;
};

const currentCapital = computed(() => {
  return shareholders.value
    .map((shareholder) => shareholder.share)
    .reduce((a, b) => a + b, 0);
});

const valid = computed(() => {
  return (
    currentCapital.value >= 2500 &&
    shareholders.value.length > 0 &&
    legalEntity.value.name &&
    legalEntity.value.name.length > 3 &&
    legalEntity.value.registryCode &&
    legalEntity.value.registryCode.length === 7 &&
    !isNaN(parseInt(legalEntity.value.registryCode)) &&
    legalEntity.value.name.length < 100
  );
});

const removeShareholder = (index: number) => {
  shareholders.value.splice(index, 1);
};

const create = () => {
  fetch("http://localhost:8000/legal-entity/", {
    method: "POST",
    body: JSON.stringify({
      ...legalEntity.value,
      capital: currentCapital.value,
      shareholders: shareholders.value,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => router.push(`/legal-entity/${data.id}`));
};
</script>

<style lang="scss" scoped>
.legal-entity-form-group {
  display: inline-flex;
  margin: 0.2rem 0;
}

.legal-entity-form-column {
  display: flex;
  flex-direction: column;
}

.legal-entity-form-field__label {
  min-width: 150px;
}

.legal-entity-form-field__input {
  min-width: 160px;
}

table {
  min-width: 400px;
}

.shareholders-table__cell,
.shareholders-table-header__cell {
  min-width: 80px;
  width: 130px;
  position: relative;
  margin: 0 5px;
}

.shareholder-autocomplete {
  position: absolute;
  background: white;

  &-results {
    margin: 0;
    border: 1px solid #eeeeee;
    height: 120px;
    min-height: 1em;
    max-height: 6em;
    overflow: auto;

    &__result {
      list-style: none;
      text-align: left;
      padding: 4px 6px;
      cursor: pointer;

      &:hover {
        background: #e8e8e8;
      }
    }
  }
}

.shareholder-share__input {
  &-group {
    display: inline-flex;
  }
  width: 90%;
}

.shareholder-type-cell {
  text-align: center;
}

.shareholder-action {
  &-icon {
    padding: 0 3px;
  }

  &__delete {
    color: #c40000;
  }
}

.btn {
  box-sizing: border-box;
  padding: 7.5px 10px;
  border-radius: 2px;
  &-inactive {
    &:hover {
      cursor: default !important;
    }
    background: gray !important;
  }
  &:hover {
    cursor: pointer;
  }
}

.create-new-entity-btn {
  &:hover {
    background: -webkit-linear-gradient(230deg, #4a934a 25%, #647eff);
  }
  color: white;
  background: #4a934a;
}

.legal-entity-actions {
  padding: 10px 0;
  display: inline-flex;
  justify-content: end;
  max-width: 600px;
  width: 100%;
}
</style>
