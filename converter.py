class converter():
    def run():
        options = [1,2,3]
        print('we:1 le:2 te:3')
        choosing = int(input('Choose a Option: '))
        while choosing not in options:
            choosing = int(input('Choose a Option: '))
        if choosing == 1:
            converter.weight()
        if choosing == 2:
            converter.lenght()
        if choosing == 3:
            converter.temperature()

    def weight():
        weight_Options = [1,2,3,4,5,6]
        number = float(input('Weight: '))
        print('mg:1 gr:2 kg:3')
        print('to:4 ou:5 po:6')
        input_weight = int(input('Input weigth?: '))
        output_weight = int(input('Output weigth?: '))
        while input_weight not in weight_Options:
            input_weight = int(input('Output weigth?: '))
        while output_weight not in weight_Options:
            output_weight = int(input('Input weigth?: '))
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
        if input_weight == 2:
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
        if input_weight == 3:
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
        if input_weight == 4:
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
        if input_weight == 5:
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
        if input_weight == 6:
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
        print(result)

    def lenght():
        lenght_Options = [1,2,3,4,5,6,7,8,9,10]
        number = float(input('Lenght: '))
        print('nm:1 um:2 mm:3')
        print('cm:4 dc:5 km:6')
        print('in:7 fo:8 ya:9')
        print('mi:9 sm:10')
        input_lenght = int(input('Input lenght?: '))
        output_lenght = int(input('Output lenght?: '))
        while input_lenght not in lenght_Options:
            input_lenght = int(input('Output lenght?: '))
        while output_lenght not in lenght_Options:
            output_lenght = int(input('Input lenght?: '))
        if input_lenght == 1:
            if input_lenght == 1:
                result = number
            elif input_lenght == 2:
                result = number
            elif input_lenght == 3:
                result = number
            elif input_lenght == 4:
                result = number
            elif input_lenght == 5:
                result = number
            elif input_lenght == 6:
                result = number
            elif input_lenght == 7:
                result = number
            elif input_lenght == 8:
                result = number
            elif input_lenght == 9:
                result = number
            elif input_lenght == 10:
                result = number
        print(result)
    
    def temperature():
        temperature_Options = [1,2,3]
        number = float(input('Temperature: '))
        print('ce:1 fa:2 ke:3')
        input_temperature = int(input('Input temperature?: '))
        output_temperature = int(input('Output temperature?: '))
        while input_temperature not in temperature_Options:
            input_temperature = int(input('Output temperature?: '))
        while output_temperature not in temperature_Options:
            output_temperature = int(input('Input temperature?: '))
        if input_temperature == 1:
            if output_temperature == 1:
                result = number
            elif output_temperature == 2:
                result = number * 9 / 5 + 32
            elif output_temperature == 3:
                result = number + 273.15
        if input_temperature == 2:
            if output_temperature == 1:
                result = (number - 32) * 5 / 9
            elif output_temperature == 2:
                result = number
            elif output_temperature == 3:
                result = (number - 32) * 5 / 9 + 273.15
        if input_temperature == 3:
            if output_temperature == 1:
                result = number - 273.15
            elif output_temperature == 2:
                result = (number - 273.15) * 5 / 9 + 32
            elif output_temperature == 3:
                result = number
        print(result)

converter.run()