<template>
  <v-hover v-slot="{ isHovering, props }">
    <v-card
      :elevation="isHovering ? 12 : 2"
      :class="{ 'on-hover': isHovering }"
      v-bind="props"
    >
      <v-img
        :src="product.src"
        height="225px"
        cover
      >
        <v-card-title class="text-h6 text-white">
          <p class="mt-4">
            {{ product.name }}
          </p>
        </v-card-title>
        <v-expand-transition>
          <div
            v-if="isHovering"
            class="d-flex transition-fast-in-fast-out bg-white v-card--reveal text-h2"
            style="height: 100%;"
          >
            <v-btn
              href="/product"
              variant="outlined"
              elevation="0"
              :color="black"
              outlined>VIEW
            </v-btn>
          </div>
        </v-expand-transition>

      </v-img>
      <v-card-actions class="d-flex flex-column align-self-center">
        <div>
          <p class="ma-0 text-body-1 font-weight-bold">
            {{ product.type }}
          </p>
          <p class="text-caption font-weight-medium">
            {{ product.price }}
          </p>
        </div>
      </v-card-actions>
    </v-card>
  </v-hover>
</template>

<script lang="ts" setup>
  interface Props { product: Object }
  const props = defineProps<Props>();
  const transparent = 'rgba(255, 255, 255, 0)';
</script>

<style scoped>
  .v-card {
    transition: opacity .4s ease-in-out;
  }

  .v-card:not(.on-hover) {
    opacity: 0.6;
  }

  .show-btns {
    color: rgba(255, 255, 255, 1) !important;
  }
</style>