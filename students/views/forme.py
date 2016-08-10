class RomanNumerals(object):

    ROMANS = (('M', 1000),

              ('CM', 900),

              ('D', 500),

              ('CD', 400),

              ('C', 100),

              ('XC', 90),

              ('L', 50),

              ('XL', 40),

              ('X', 10),

              ('IX', 9),

              ('V', 5),

              ('IV', 4),

              ('I', 1))
    @classmethod
    def from_roman(self, roman):
        normal_ver = 0
        for rom_num, value in self.ROMANS:
            while roman.startswith(rom_num):
                normal_ver += value
                roman = roman[len(rom_num):]
        return normal_ver

    @classmethod
    def to_roman(self, number):
        number = int(number)
        print number
        roman_ver = ''
        for rom_num, value in self.ROMANS:
            while number >= value:
                number -= value
                roman_ver += rom_num
        return roman_ver




print RomanNumerals.to_roman('1666')
print RomanNumerals.from_roman('MDCLXVI')
