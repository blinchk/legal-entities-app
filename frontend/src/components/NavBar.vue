<template>
  <nav class="nav">
    <div class="nav__logo">
      <router-link class="nav-home nav__link" to="/">Äriühingud</router-link>
    </div>
    <div class="nav-links">
      <router-link class="nav__link" to="/" exact-active-class="current-link"
        ><font-awesome-icon icon="home" size="xs" /> Avaleht</router-link
      >
      <router-link
        class="nav__link"
        to="/legal-entity/create"
        active-class="current-link"
      >
        <font-awesome-icon icon="add" size="xs" /> Asutamine</router-link
      >
    </div>
  </nav>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "NavBar",
});
</script>

<style scoped lang="scss">
.nav {
  width: 100%;
  justify-content: space-between;
  padding: 10px 32px;
  display: inline-flex;
  align-items: center;
  border-bottom: 0.2rem solid rgba(60, 60, 60, 0.12);

  &__logo {
    font-size: 24px;
  }

  &-links {
    display: inline-flex;
    justify-content: space-evenly;
  }

  &__link {
    padding: 0 0.5rem 0.5rem;
    margin: 0 0 0 0.1rem;
  }
}

.current-link {
  border-bottom: 0.14rem solid #000000;
  border-collapse: separate;
}
</style>
