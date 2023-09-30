<template>
  <v-col cols="12">
    <v-card-text
      tile
      outlined
    >
      <v-card-title class="subheading ">Deals of the Day</v-card-title>
      <v-divider></v-divider>
      <v-row>
        <v-col cols="12" md="3" sm="6" xs="6" class="text-center">
          <v-hover
            v-slot:default="{ hover }"
            open-delay="200"
          >
            <v-card
              :elevation="hover ? 16 : 2"
          >
            <v-img
              class="white--text align-end"
              height="200px"
              src="@/assets/img/home/deal1.jpg"
            >
              <v-card-title>Bags & Purses </v-card-title>
            </v-img>

            <v-card-text class="text--primary text-center">
              <div>Upto 60% + Extra 10%</div>
              <div>Baggit, Zara, Fossil</div>
            </v-card-text>

            <div class="text-center">
              <v-btn
                href="/shop"
                class="ma-2"
                outlined
                color="info"
              >
                Explore
              </v-btn>
            </div>
          </v-card>
          </v-hover>
        </v-col>
        <v-col cols="12" md="3" sm="6" xs="6" class="text-center">
          <v-hover
            v-slot:default="{ hover }"
            open-delay="200"
          >
            <v-card
              :elevation="hover ? 16 : 2"
            >
            <v-img
              class="white--text align-end"
              height="200px"
              src="@/assets/img/home/deal2.jpg"
            >
              <v-card-title>T-Shirt </v-card-title>
            </v-img>

            <v-card-text class="text--primary text-center">
              <div>Upto 50%</div>
              <div>Zara, Selected, Celio</div>
            </v-card-text>

            <div class="text-center">
              <v-btn href="/shop"
                class="ma-2"
                outlined
                color="info"
              >
                Explore
              </v-btn>
            </div>
          </v-card>
          </v-hover>
        </v-col>
        <v-col cols="12" md="3" sm="6" xs="6" class="text-center" >
          <v-hover
            v-slot:default="{ hover }"
            open-delay="200"
          >
            <v-card
              :elevation="hover ? 16 : 2"
            >
            <v-img
              class="white--text align-end"
              height="200px"
              src="../assets/img/home/deal3.jpg"
            >
              <v-card-title>Jeans </v-card-title>
            </v-img>

            <v-card-text class="text--primary text-center">
              <div>Upto 60% + Extra 10%</div>
              <div>Jack & Jones, Levis</div>
            </v-card-text>

            <div class="text-center">
              <v-btn href="/shop"
                class="ma-2"
                outlined
                color="info"
              >
                Explore
              </v-btn>
            </div>
          </v-card>
          </v-hover>
        </v-col>
        <v-col cols="12" md="3" sm="6" xs="6" class="text-center" >
          <v-hover
            v-slot:default="{ hover }"
            open-delay="200"
          >
            <v-card
              :elevation="hover ? 16 : 2"
            >
            <v-img
              class="white--text align-end"
              height="200px"
              src="@/assets/img/home/deal4.jpg"
            >
              <v-card-title>Shoes </v-card-title>
            </v-img>

            <v-card-text class="text--primary text-center">
              <div>Upto 60% + Extra 10%</div>
              <div>Nike, Adidas, Puma</div>
            </v-card-text>

            <div class="text-center">
              <v-btn href="/shop"
                class="ma-2"
                outlined
                color="info"
              >
                Explore
              </v-btn>
            </div>
          </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-card-text>
  </v-col>
</template>