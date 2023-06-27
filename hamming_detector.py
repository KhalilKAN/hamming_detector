def calculate_parity_bits(bits_inf):
    # Calcular el número de bits de paridad que posee el mensaje
    p = 0
    while 2 ** p < bits_inf: #ya que bits_inf = i + p
        p += 1
    return p

def generate_table_ones_values(p):
    ones_values = 2**(p-1) #por ejemplo, si p=4, ones_values empieza en 8, despues vale 4, despues 2, despues 1. Es generico
    table_values = []
    for i in range(p):
        table_values.append(([0] * 2**i + [1] * 2**i) * ones_values)
        ones_values = ones_values//2
    return table_values

def get_controlled_positions(table_ones_values, message):
    controlled_positions = []
    for i in range(len(table_ones_values)):
        positions = []
        for j in range(len(table_ones_values[i])):
            if(table_ones_values[i][j] == 1 and j <= len(message)):
                positions.append(j)
        controlled_positions.append(positions)
    return controlled_positions

def get_position_error(controlled_positions):
    inverted_message = message[::-1]
    message_fix = "_" + inverted_message #porque los indices deben empezar en 1, alto fix pa
    index_errors = []
    for i in range(len(controlled_positions)):
        acum = 0
        for j in range(len(controlled_positions[i])):
            acum += int(message_fix[controlled_positions[i][j]])        
        index_errors.insert(0, 0 if acum % 2 == 0 else 1)

    index_error_string = ''.join(str(index) for index in index_errors)
    position_decimal = int(index_error_string, 2)
    return position_decimal

def hamming_detector(message):
    bits_inf = len(message)
    
    p = calculate_parity_bits(bits_inf)
    table_ones_values = generate_table_ones_values(p)
    controlled_positions = get_controlled_positions(table_ones_values, message)
    position_decimal = get_position_error(controlled_positions)
    
    if(position_decimal == 0):
        print("No se encontró errores en el mensaje: ", message)
    else:
        print("Hay un error en la posición: ", position_decimal)


message = "0100011"
hamming_detector(message)
