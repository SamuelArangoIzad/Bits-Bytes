
class code:

  #Method by traslate from caracter to binary
  @staticmethod
  def string_to_bits(text):

    #Tranforme the caracter to binary
    bits=''.join(format(ord(char),'08b') for char in text)
    return bits


  #Traslate binary to string
  @staticmethod
  def bits_to_string(bits):

    byte_array=[bits[ii:ii+8] for ii in range(0, len(bits), 8)]
    cadena = ''.join([chr(int(byte,2)) for byte in byte_array])