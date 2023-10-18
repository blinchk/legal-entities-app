// eslint-disable-next-line
// @ts-ignore
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import NewLegalEntityView from "@/views/NewLegalEntityView.vue";
import LegalEntityView from "@/views/LegalEntityView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Avaleht",
    component: HomeView,
  },
  {
    path: "/legal-entity/create",
    name: "Asutamine",
    component: NewLegalEntityView,
  },
  {
    path: "/legal-entity/:id",
    name: "Andmete vaade",
    component: LegalEntityView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
