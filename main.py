class main_menu():
    def run():
        user_options = [1,2,3]
        print('math:1')
        print('physics:2')
        print('exit:3')
        user_input = int(input('Choose one Option: '))
        while user_input not in user_options:
            user_input = int(input('Choose one Option: '))
        if user_input == 1:
            print('\n', end='')
            main_menu.math()
        elif user_input == 2:
            print('\n', end='')
            main_menu.physics()
        elif user_input == 3:
            exit()

    def math():
        user_options = [1]
        print('converter:1')
        user_input = int(input('Choose one Option: '))
        while user_input not in user_options:
            user_input = int(input('Choose one Option: '))
        if user_input == 1:
            print('\n', end='')
            converter.run()
    def physics():
        print('No physics yet.')
        print('\n', end='')
        main_menu.run()

# Math
class converter():
    def run():
        options = [1,2,3]
        print('we:1 le:2 te:3')
        choosing = int(input('Choose a Option: '))
        while choosing not in options:
            choosing = int(input('Choose a Option: '))
        if choosing == 1:
            print('\n', end='')
            converter.weight()
        elif choosing == 2:
            print('\n', end='')
            converter.lenght()
        elif choosing == 3:
            print('\n', end='')
            converter.temperature()

    def weight():
        weight_Options = [1,2,3,4,5,6]
        number = float(input('Weight: '))
        print('mg:1 gr:2 kg:3')
        print('to:4 ou:5 po:6')
        input_weight = int(input('Input weigth?: '))
        while input_weight not in weight_Options:
            input_weight = int(input('Input weigth?: '))
        output_weight = int(input('Output weigth?: '))
        while output_weight not in weight_Options:
            output_weight = int(input('Output weigth?: '))
        if input_weight == 1:
            if output_weight == 1:
                result = number
            elif output_weight == 2:
                result = number / 1000
            elif output_weight == 3:
                result = number / 1000000
            elif output_weight == 4:
                result = number / 1000000000
            elif output_weight == 5:
                result = number / 28350
            elif output_weight == 6:
                result = number / 453600
        elif input_weight == 2:
            if output_weight == 1:
                result = number * 1000
            elif output_weight == 2:
                result = number
            elif output_weight == 3:
                result = number / 1000
            elif output_weight == 4:
                result = number / 1000000
            elif output_weight == 5:
                result = number / 28.35
            elif output_weight == 6:
                result = number / 453.6
        elif input_weight == 3:
            if output_weight == 1:
                result = number * 1000000
            elif output_weight == 2:
                result = number * 1000
            elif output_weight == 3:
                result = number
            elif output_weight == 4:
                result = number / 1000
            elif output_weight == 5:
                result = number * 35.274
            elif output_weight == 6:
                result = number / 2.205
        elif input_weight == 4:
            if output_weight == 1:
                result = number * 1000000000
            elif output_weight == 2:
                result = number * 1000000
            elif output_weight == 3:
                result = number * 1000
            elif output_weight == 4:
                result = number
            elif output_weight == 5:
                result = number * 35270
            elif output_weight == 6:
                result = number / 2205
        elif input_weight == 5:
            if output_weight == 1:
                result = number * 28350
            elif output_weight == 2:
                result = number * 28.35
            elif output_weight == 3:
                result = number / 35.274
            elif output_weight == 4:
                result = number / 35270
            elif output_weight == 5:
                result = number
            elif output_weight == 6:
                result = number / 16
        elif input_weight == 6:
            if output_weight == 1:
                result = number * 453600
            elif output_weight == 2:
                result = number * 453.6
            elif output_weight == 3:
                result = number / 2.205
            elif output_weight == 4:
                result = number / 2205
            elif output_weight == 5:
                result = number * 16
            elif output_weight == 6:
                result = number
        print('\n', end='')
        print(result)

    def lenght():
        lenght_Options = [1,2,3,4,5,6,7,8,9,10,11,12]
        number = float(input('Lenght: '))
        print('nm:1 um:2 mm:3')
        print('cm:4 dc:5 mt:6')
        print('km:7 in:8 fo:9')
        print('ya:10 mi:11 sm:12')
        input_lenght = int(input('Input lenght?: '))
        while input_lenght not in lenght_Options:
            input_lenght = int(input('Output lenght?: '))
        output_lenght = int(input('Output lenght?: '))
        while output_lenght not in lenght_Options:
            output_lenght = int(input('Input lenght?: '))
        if input_lenght == 1: # Nanometer
            if output_lenght == 1: # Nanometer -> Nanometer
                result = number
            elif output_lenght == 2: # Nanometer -> Mikrometer
                result = number
            elif output_lenght == 3: # Nanometer -> Millimeter
                result = number
            elif output_lenght == 4: # Nanometer -> Centimeter
                result = number
            elif output_lenght == 5: # Nanometer -> Decimeter
                result = number
            elif output_lenght == 6: # Nanometer -> Meter
                result = number
            elif output_lenght == 7: # Nanometer -> Kilometer
                result = number
            elif output_lenght == 8: # Nanometer -> Inches
                result = number
            elif output_lenght == 9: # Nanometer -> Foot
                result = number
            elif output_lenght == 10: # Nanometer -> Yard
                result = number
            elif output_lenght == 11: # Nanometer -> Mile
                result = number
            elif output_lenght == 12: # Nanometer -> Sea Mile
                result = number
        if input_lenght == 2: # Mikrometer
            if output_lenght == 1: # Mikrometer -> Nanometer
                result = number
            elif output_lenght == 2: # Mikrometer -> Mikrometer
                result = number
            elif output_lenght == 3: # Mikrometer -> Millimeter
                result = number
            elif output_lenght == 4: # Mikrometer -> Centimeter
                result = number
            elif output_lenght == 5: # Mikrometer -> Decimeter
                result = number
            elif output_lenght == 6: # Mikrometer -> Meter
                result = number
            elif output_lenght == 7: # Mikrometer -> Kilometer
                result = number
            elif output_lenght == 8: # Mikrometer -> Inches
                result = number
            elif output_lenght == 9: # Mikrometer -> Foot
                result = number
            elif output_lenght == 10: # Mikrometer -> Yard
                result = number
            elif output_lenght == 11: # Mikrometer -> Mile
                result = number
            elif output_lenght == 12: # Mikrometer -> Sea Mile
                result = number
        if input_lenght == 3: # Millimeter
            if output_lenght == 1: # Millimeter -> Nanometer
                result = number
            elif output_lenght == 2: # Millimeter -> Mikrometer
                result = number
            elif output_lenght == 3: # Millimeter -> Millimeter
                result = number
            elif output_lenght == 4: # Millimeter -> Centimeter
                result = number
            elif output_lenght == 5: # Millimeter -> Decimeter
                result = number
            elif output_lenght == 6: # Millimeter -> Meter
                result = number
            elif output_lenght == 7: # Millimeter -> Kilometer
                result = number
            elif output_lenght == 8: # Millimeter -> Inches
                result = number
            elif output_lenght == 9: # Millimeter -> Foot
                result = number
            elif output_lenght == 10: # Millimeter -> Yard
                result = number
            elif output_lenght == 11: # Millimeter -> Mile
                result = number
            elif output_lenght == 12: # Millimeter -> Sea Mile
                result = number
        if input_lenght == 4: # Centimeter
            if output_lenght == 1: # Centimeter -> Nanometer
                result = number
            elif output_lenght == 2: # Centimeter -> Mikrometer
                result = number
            elif output_lenght == 3: # Centimeter -> Millimeter
                result = number
            elif output_lenght == 4: # Centimeter -> Centimeter
                result = number
            elif output_lenght == 5: # Centimeter -> Decimeter
                result = number
            elif output_lenght == 6: # Centimeter -> Meter
                result = number
            elif output_lenght == 7: # Centimeter -> Kilometer
                result = number
            elif output_lenght == 8: # Centimeter -> Inches
                result = number
            elif output_lenght == 9: # Centimeter -> Foot
                result = number
            elif output_lenght == 10: # Centimeter -> Yard
                result = number
            elif output_lenght == 11: # Centimeter -> Mile
                result = number
            elif output_lenght == 12: # Centimeter -> Sea Mile
                result = number
        if input_lenght == 5: # Decimeter
            if output_lenght == 1: # Decimeter -> Nanometer
                result = number
            elif output_lenght == 2: # Decimeter -> Mikrometer
                result = number
            elif output_lenght == 3: # Decimeter -> Millimeter
                result = number
            elif output_lenght == 4: # Decimeter -> Centimeter
                result = number
            elif output_lenght == 5: # Decimeter -> Decimeter
                result = number
            elif output_lenght == 6: # Decimeter -> Meter
                result = number
            elif output_lenght == 7: # Decimeter -> Kilometer
                result = number
            elif output_lenght == 8: # Decimeter -> Inches
                result = number
            elif output_lenght == 9: # Decimeter -> Foot
                result = number
            elif output_lenght == 10: # Decimeter -> Yard
                result = number
            elif output_lenght == 11: # Decimeter -> Mile
                result = number
            elif output_lenght == 12: # Decimeter -> Sea Mile
                result = number
        print('\n', end='')
        print(result)
    
    def temperature():
        temperature_Options = [1,2,3]
        number = float(input('Temperature: '))
        print('ce:1 fa:2 ke:3')
        input_temperature = int(input('Input temperature?: '))
        while input_temperature not in temperature_Options:
            input_temperature = int(input('Output temperature?: '))
        output_temperature = int(input('Output temperature?: '))
        while output_temperature not in temperature_Options:
            output_temperature = int(input('Input temperature?: '))
        if input_temperature == 1:
            if output_temperature == 1:
                result = number
            elif output_temperature == 2:
                result = number * 9 / 5 + 32
            elif output_temperature == 3:
                result = number + 273.15
        elif input_temperature == 2:
            if output_temperature == 1:
                result = (number - 32) * 5 / 9
            elif output_temperature == 2:
                result = number
            elif output_temperature == 3:
                result = (number - 32) * 5 / 9 + 273.15
        elif input_temperature == 3:
            if output_temperature == 1:
                result = number - 273.15
            elif output_temperature == 2:
                result = (number - 273.15) * 5 / 9 + 32
            elif output_temperature == 3:
                result = number
        print('\n', end='')
        print(result)

main_menu.run()