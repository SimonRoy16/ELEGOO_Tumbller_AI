// Wokwi Custom Chip - For docs and examples see:
// https://docs.wokwi.com/chips-api/getting-started
//
// SPDX-License-Identifier: MIT
// Copyright 2023 Simon Roy

// Input / output names must match the pins defined in the chip's JSON file:
module wokwi (
    input wire AIN1,  // Channel A input 1
    input wire AIN2,  // Channel A input 2
    input wire PWMA,  // Channel A PWM input
    input wire BIN1,  // Channel B input 1
    input wire BIN2,  // Channel B input 2
    input wire PWMB,  // Channel B PWM input
    input wire STBY,  // Standby input
    output reg AO1,   // Channel A output 1
    output reg AO2,   // Channel A output 2
    output reg BO1,   // Channel B output 1
    output reg BO2    // Channel B output 2
);

    // Internal combinational logic for each channel
    always @(*) begin
        // Default outputs
        AO1 = 1'b0;
        AO2 = 1'b0;
        BO1 = 1'b0;
        BO2 = 1'b0;

        // Standby mode
        if (STBY == 1'b0) begin
            // High impedance state
            AO1 = 1'bz;
            AO2 = 1'bz;
            BO1 = 1'bz;
            BO2 = 1'bz;
        end else begin
            // Channel A Control
            if (AIN1 == 1'b1 && AIN2 == 1'b1) begin
              // Short Brake
              AO1 = 1'b0;
              AO2 = 1'b0;
            end else if (AIN1 == 1'b0 && AIN2 == 1'b0) begin
              // Stop
              AO1 = 1'bz;
              AO2 = 1'bz;
            end else if (PWMA == 1'b1) begin
              if (AIN1 == 1'b1 && AIN2 == 1'b0) begin
                // CW
                AO1 = 1'b1;
                AO2 = 1'b0;
              end else if (AIN1 == 1'b0 && AIN2 == 1'b1) begin
                // CCW
                AO1 = 1'b0;
                AO2 = 1'b1;
              end
            end else begin
              // Short Brake
              AO1 = 1'b0;
              AO2 = 1'b0;
            end

            // Channel B Control
            if (BIN1 == 1'b1 && BIN2 == 1'b1) begin
              // Short Brake
              BO1 = 1'b0;
              BO2 = 1'b0;
            end else if (BIN1 == 1'b0 && BIN2 == 1'b0) begin
              // Stop
              BO1 = 1'bz;
              BO2 = 1'bz;
            end else if (PWMB == 1'b1) begin
              if (BIN1 == 1'b1 && BIN2 == 1'b0) begin
                // CW
                BO1 = 1'b1;
                BO2 = 1'b0;
              end else if (BIN1 == 1'b0 && BIN2 == 1'b1) begin
                // CCW
                BO1 = 1'b0;
                BO2 = 1'b1;
              end
            end else begin
              // Short Brake
              BO1 = 1'b0;
              BO2 = 1'b0;
            end
        end
    end
endmodule
