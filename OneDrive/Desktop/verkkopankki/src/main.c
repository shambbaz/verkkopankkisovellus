#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

#define MAX_FILENAME 50
#define MAX_PIN 10

// Funktio käsittelee API:n vastauksen
size_t write_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    strcat((char *)userp, (char *)contents);
    return size * nmemb;
}

// Funktio lähettää API-pyynnön ja palauttaa vastauksen
int send_api_request(const char *url, const char *data, char *response) {
    CURL *curl;
    CURLcode res;

    curl = curl_easy_init();
    if (curl) {
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");

        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, response);

        res = curl_easy_perform(curl);

        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);

        if (res != CURLE_OK) {
            fprintf(stderr, "cURL error: %s\n", curl_easy_strerror(res));
            return 0;
        }
        return 1;
    }
    return 0;
}

// Tarkistaa saldon API:sta
int tarkista_saldo_api(char *tilinumero, char *pin, int *saldo) {
    char url[] = "http://127.0.0.1:5000/api/balance";
    char postdata[100], response[100] = "";

    snprintf(postdata, sizeof(postdata), "{\"account\": \"%s\", \"pin\": \"%s\"}", tilinumero, pin);

    if (!send_api_request(url, postdata, response)) {
        printf("Saldon tarkistus epäonnistui.\n");
        return 0;
    }

    // Lue vastaus JSON-muodosta
    if (strstr(response, "balance") != NULL) {
        sscanf(response, "{\"balance\":%d}", saldo);
        return 1;
    }

    printf("Virheellinen vastaus API:lta: %s\n", response);
    return 0;
}

// Nostaa rahaa API:n kautta
int nosta_rahaa_api(char *tilinumero, char *pin, int summa, int *saldo) {
    char url[] = "http://127.0.0.1:5000/api/withdraw";
    char postdata[150], response[100] = "";

    snprintf(postdata, sizeof(postdata), "{\"account\": \"%s\", \"pin\": \"%s\", \"amount\": %d}", tilinumero, pin, summa);

    if (!send_api_request(url, postdata, response)) {
        printf("Nosto epäonnistui.\n");
        return 0;
    }

    if (strstr(response, "new_balance") != NULL) {
        sscanf(response, "{\"withdrawn\":%*d,\"new_balance\":%d}", saldo);
        return 1;
    }

    printf("Virheellinen vastaus API:lta: %s\n", response);
    return 0;
}

// Tallettaa rahaa API:n kautta
int talleta_rahaa_api(char *tilinumero, char *pin, int summa, int *saldo) {
    char url[] = "http://127.0.0.1:5000/api/deposit";
    char postdata[150], response[100] = "";

    snprintf(postdata, sizeof(postdata), "{\"account\": \"%s\", \"pin\": \"%s\", \"amount\": %d}", tilinumero, pin, summa);

    if (!send_api_request(url, postdata, response)) {
        printf("Talletus epäonnistui.\n");
        return 0;
    }

    if (strstr(response, "new_balance") != NULL) {
        sscanf(response, "{\"deposited\":%*d,\"new_balance\":%d}", saldo);
        return 1;
    }

    printf("Virheellinen vastaus API:lta: %s\n", response);
    return 0;
}

int valikko(char *tilinumero, char *pin, int saldo) {
    int valinta;

    do {
        printf("\nValitse toiminto:\n");
        printf("1. Tarkista saldo\n");
        printf("2. Nosta rahaa\n");
        printf("3. Talleta rahaa\n");
        printf("4. Lopeta\n");
        printf("Valintasi: ");
        if (scanf("%d", &valinta) != 1) {
            printf("Virheellinen syöte. Käytä vain numeroita.\n");
            while (getchar() != '\n');
            continue;
        }

        switch (valinta) {
            case 1:
                if (tarkista_saldo_api(tilinumero, pin, &saldo)) {
                    printf("Tilisi saldo on: %d euroa\n", saldo);
                }
                break;
            case 2: {
                int summa;
                printf("Syötä nostettava summa (20-1000 euroa, 10 euron välein): ");
                scanf("%d", &summa);
                if (nosta_rahaa_api(tilinumero, pin, summa, &saldo)) {
                    printf("Nostit %d euroa. Uusi saldo: %d euroa\n", summa, saldo);
                }
                break;
            }
            case 3: {
                int summa;
                printf("Syötä talletettava summa: ");
                scanf("%d", &summa);
                if (talleta_rahaa_api(tilinumero, pin, summa, &saldo)) {
                    printf("Talletit %d euroa. Uusi saldo: %d euroa\n", summa, saldo);
                }
                break;
            }
            case 4:
                printf("Kiitos, että käytit automaattia. Hyvää päivän jatkoa!\n");
                break;
            default:
                printf("Virheellinen valinta. Yritä uudelleen.\n");
        }
    } while (valinta != 4);

    return saldo;
}

int main() {
    char tilinumero[MAX_FILENAME];
    char pin[MAX_PIN];
    int saldo;

    printf("Syötä tilinumero: ");
    scanf("%s", tilinumero);

    printf("Syötä PIN-koodi: ");
    scanf("%s", pin);

    if (!tarkista_saldo_api(tilinumero, pin, &saldo)) {
        printf("Ohjelma päättyy virheellisen syötteen vuoksi.\n");
        return 1;
    }

    valikko(tilinumero, pin, saldo);
    return 0;
}
