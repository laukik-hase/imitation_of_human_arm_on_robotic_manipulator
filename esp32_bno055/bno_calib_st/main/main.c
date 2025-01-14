#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>

#include "sdkconfig.h"

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "bno055_utils.h"

static const char *TAG = "bno_calib_st";

/*
    **Euler angle axes** -- Refer bno055_init_routine(...)
    Pitch: Y-Axis
    Roll: X-Axis
    Heading: Z-Axis
*/

void app_main()
{
    ESP_LOGI(TAG, "Hello From ESP32!");
    ESP_ERROR_CHECK(i2c_master_init());

    // Initializing the NVS and loading the already defined calibration matrix
    // Refer: nvs_utils.c
    ESP_ERROR_CHECK(nvs_init());
    // ESP_ERROR_CHECK(nvs_load_calib_data()); No need to load calib data here

    uint8_t sensors = ACCEL | GYRO | MAG;

    struct bno055_t link;
    i2c_mux_select(MPU_PALM); // Connect to PALM
    bno055_init_routine(&link, sensors, MPU_PALM);

    struct bno055_euler_float_t link_angle;
    vTaskDelay(2000 / portTICK_PERIOD_MS);

    //NOTE: After calibration, roll and pitch should be 0 on a flat surface while yaw should be 
    // 0 deg while pointing to the geographic north pole

    while (1)
    {
        bno055_get_rph(&link_angle);
        ESP_LOGD(TAG, "Roll: %0.4f | Pitch: %0.4f | Yaw: %0.4f", link_angle.r, link_angle.p, link_angle.h);
    }
}
