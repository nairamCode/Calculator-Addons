class umrechner():
    def run():
        options = [1,2]
        print('we:1')
        choosing = int(input('Choose a Option: '))
        while choosing not in options:
            choosing = int(input('Choose a Option: '))
        if choosing == 1:
            umrechner.weight()

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

umrechner.run()