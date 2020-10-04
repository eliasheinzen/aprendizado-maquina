class Range():
    """
    Extract characteristics from Sideshow Bob character
    """

    def bob_is_hair(self, red, green, blue): # 181, 12, 44
        return 171 <= red <= 191 and 2 <= green <= 22 and 34 <= blue <= 54

    def bob_is_pants(self, red, green, blue): # 51, 78, 43
        return 41 <= red <= 61 and 68 <= green <= 88 and 33 <= blue <= 53

    def bob_is_shirt(self, red, green, blue): # 83, 139, 171
        return 73 <= red <= 93 and 129 <= green <= 149 and 161 <= blue <= 181

    """
    Extract characteristics from Krusty the Clown
    """

    def krusty_is_hair(self, red, green, blue): # 29, 101, 90
        return 19 <= red <= 39 and 91 <= green <= 111 and 80 <= blue <= 100

    def krusty_is_pants(self, red, green, blue): # 180, 213, 140
        return 170 <= red <= 190 and 203 <= green <= 223 and 130 <= blue <= 150

    def krusty_is_shirt(self, red, green, blue): # 181, 186, 214
        return 171 <= red <= 191 and 176 <= green <= 196 and 204 <= blue <= 224
