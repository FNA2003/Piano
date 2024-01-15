from pygame import mixer

MUSIC_ROUTE = "./Sounds/"

mixer.init()

KEYS = {
    1073741882:  
        [mixer.Sound(MUSIC_ROUTE+"C2.mp3") , "C2"]
     , 
    1073741883: 
        [mixer.Sound(MUSIC_ROUTE+"Db2.mp3"), "Db2" ]
     , 
    1073741884: 
        [mixer.Sound(MUSIC_ROUTE+"D2.mp3"), "D2"]
     , 
    1073741885: 
        [mixer.Sound(MUSIC_ROUTE+"Eb2.mp3"), "Eb2"]
     ,  
    1073741886: 
        [mixer.Sound(MUSIC_ROUTE+"E2.mp3"), "E2"]
     , 
    1073741887: 
        [mixer.Sound(MUSIC_ROUTE+"F2.mp3"), "F2"]
     ,  
    1073741888: 
        [mixer.Sound(MUSIC_ROUTE+"Gb2.mp3"), "Gb2"]
     , 
    1073741889: 
        [mixer.Sound(MUSIC_ROUTE+"G2.mp3"), "G2"]
     ,   
    1073741890: 
        [mixer.Sound(MUSIC_ROUTE+"Ab2.mp3"), "Ab2"]
     ,  
    1073741891: 
        [mixer.Sound(MUSIC_ROUTE+"A2.mp3"), "A2"]
     , 
    1073741892: 
        [mixer.Sound(MUSIC_ROUTE+"Bb2.mp3"), "Bb2"]
     ,  
    1073741893: 
        [mixer.Sound(MUSIC_ROUTE+"B2.mp3"), "B2"]
     ,  
    49: 
        [mixer.Sound(MUSIC_ROUTE+"C3.mp3"), "C3"]
     , 
    50: 
        [mixer.Sound(MUSIC_ROUTE + "Db3.mp3"), "Db3"]
     ,   
    51: 
        [mixer.Sound(MUSIC_ROUTE+"D3.mp3"), "D3"]
     , 
    52: 
        [mixer.Sound(MUSIC_ROUTE+"Eb3.mp3"), "Eb3"]
     , 
    53: 
        [mixer.Sound(MUSIC_ROUTE+"E3.mp3"), "E3"]
     ,  
    54: 
        [mixer.Sound(MUSIC_ROUTE+"F3.mp3"), "F3"]
     ,  
    55: 
        [mixer.Sound(MUSIC_ROUTE+"Gb3.mp3"), "Gb3"]
     ,  
    56: 
        [mixer.Sound(MUSIC_ROUTE+"G3.mp3"), "G3"]
     ,  
    57: 
        [mixer.Sound(MUSIC_ROUTE+"Ab3.mp3"), "Ab3"]
     ,
    48: 
        [mixer.Sound(MUSIC_ROUTE+"A3.mp3"), "A3"]
     ,  
    39: 
        [mixer.Sound(MUSIC_ROUTE+"Bb3.mp3"), "Bb3"]
     ,
    191 : 
        [mixer.Sound(MUSIC_ROUTE+"B3.mp3"), "B3"]
     , 
    113: 
        [mixer.Sound(MUSIC_ROUTE+"C4.mp3"), "C4"]
     ,
    119: 
        [mixer.Sound(MUSIC_ROUTE+"Db4.mp3"), "Db4"]
     ,  
    101: 
        [mixer.Sound(MUSIC_ROUTE+"D4.mp3"), "D4"]
     , 
    114: 
        [mixer.Sound(MUSIC_ROUTE+"Eb4.mp3"), "Eb4"]
     ,  
    116: 
        [mixer.Sound(MUSIC_ROUTE+"E4.mp3"), "E4"]
     ,
    121: 
        [mixer.Sound(MUSIC_ROUTE+"F4.mp3"), "F4"]
     ,  
    117: 
        [mixer.Sound(MUSIC_ROUTE+"Gb4.mp3"), "Gb4"]
     ,
    105: 
        [mixer.Sound(MUSIC_ROUTE+"G4.mp3"), "G4"] 
     ,  
    111: 
        [mixer.Sound(MUSIC_ROUTE+"Ab4.mp3"), "Ab4"]
     ,  
    112: 
        [mixer.Sound(MUSIC_ROUTE+"A4.mp3"), "A4"]
     ,  
    180: 
        [mixer.Sound(MUSIC_ROUTE+"Bb4.mp3"), "Bb4"]
     , 
    43: 
        [mixer.Sound(MUSIC_ROUTE+"B4.mp3"), "B4"]
     , 
    97: 
        [mixer.Sound(MUSIC_ROUTE+"C5.mp3"), "C5"]
     , 
    115: 
        [mixer.Sound(MUSIC_ROUTE+"Db5.mp3"), "Db5"]
     ,  
    100: 
        [mixer.Sound(MUSIC_ROUTE+"D5.mp3"), "D5"]
     , 
    102: 
        [mixer.Sound(MUSIC_ROUTE+"Eb5.mp3"), "Eb5"]
     , 
    103: 
        [mixer.Sound(MUSIC_ROUTE+"E5.mp3"), "E5"]
     ,  
    104: 
        [mixer.Sound(MUSIC_ROUTE+"F5.mp3"), "F5"]
     ,  
    106: 
        [mixer.Sound(MUSIC_ROUTE+"Gb5.mp3"), "Gb5"]
     ,  
    107: 
        [mixer.Sound(MUSIC_ROUTE+"G5.mp3"), "G5"]
     , 
    108: 
        [mixer.Sound(MUSIC_ROUTE+"Ab5.mp3"), "Ab5"]
     , 
    241: 
        [mixer.Sound(MUSIC_ROUTE+"A5.mp3"), "A5"]
     ,  
    123: 
        [mixer.Sound(MUSIC_ROUTE+"Bb5.mp3"), "Bb5"]
     , 
    125: 
        [mixer.Sound(MUSIC_ROUTE+"B5.mp3"), "B5"]
     , 
    60: 
        [mixer.Sound(MUSIC_ROUTE+"C6.mp3"), "C6"]
     ,
    122: 
        [mixer.Sound(MUSIC_ROUTE+"Db6.mp3"), "Db6"]
     ,  
    120: 
        [mixer.Sound(MUSIC_ROUTE+"D6.mp3"), "D6"]
     ,
    99: 
        [mixer.Sound(MUSIC_ROUTE+"Eb6.mp3"), "Eb6"]
     , 
    118: 
        [mixer.Sound(MUSIC_ROUTE+"E6.mp3"), "E6"]
     , 
    98: 
        [mixer.Sound(MUSIC_ROUTE+"F6.mp3"), "F6"]
     ,  
    110: 
        [mixer.Sound(MUSIC_ROUTE+"Gb6.mp3"), "Gb6"]
     ,  
    109: 
        [mixer.Sound(MUSIC_ROUTE+"G6.mp3"), "G6"]
     ,  
    44: 
        [mixer.Sound(MUSIC_ROUTE+"Ab6.mp3"), "Ab6"]
     , 
    46: 
        [mixer.Sound(MUSIC_ROUTE+"A6.mp3"), "A6"]
     , 
    45: 
        [mixer.Sound(MUSIC_ROUTE+"Bb6.mp3"), "Bb6"]
     , 
    1073742053: 
        [mixer.Sound(MUSIC_ROUTE+"B6.mp3"), "B6"]
}