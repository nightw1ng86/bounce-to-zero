# Oyun kodlaması bu dosyadadir.

# Oyundaki karakterleri tanimla. Renk argumani karakterin
# isminin rengini belirler.
define mc = Character("Liam")
define e = Character("Eli")
define h = Character("Hırsız")
image bg yenidunya = Transform("images/yenidunya.jpg", xysize=(config.screen_width, config.screen_height))
image bg merdiven = Transform("images/merdiven.jpg", xysize=(config.screen_width, config.screen_height))
image hirsiz = "images/hirsiz.png"
image eli = "images/Eli.png"
image eli sasirmis = "images/elisasirmis.png"
image eli happy = "images/elihappy.png"
image eli wedding = "images/eliwedding"
image bg dugun = Transform("images/dugun.png", xysize=(config.screen_width, config.screen_height))

label start:
   scene bg merdiven
   with fade


   mc "Hayat bir merdiven gibi."

   mc "Sadece tırmanmaya devam etmen gerek."

   mc "Aşırı düşünmeye başlarsan sonraki adımı atmakta zorluk yaşarsın."

   mc "Ayrılan yollar yok."

   mc "Yapmadığınız eylemlerden pişman olmanın bir anlamı yok."

   mc "Hayatın bir dizi seçimden ibaret olduğunu söylerler."

   mc "Ama bu oyun bağımlılarının uydurduğu bir saçmalık."

   mc "Dün bugüne, bugün de yarına götürür."

   mc "Geçmişi yazan geleceği de yazar."

   mc "Birer birer adımlar atın."

   mc "Önünüzde ne var? Oraya varana kadar bilemezsiniz."

   mc "Gene sinir bozucu bir gün olacağa benziyor, bu merdivenler de bir türlü bitmedi arkadaş!"

   mc "Neyse son iki basama-"
   play sound "audio/düşme.mp3"
   with fade
   #çarpma sesi eklenecek
   pause 1.0
   scene bg yenidunya
   with fade
label label_2:
    play sound "audio/rbd.mp3"

    scene bg yenidunya with fade

    mc "Burası da nere?"
    mc "Bir Discord moderatörünün fantazisine mi ışınlandım?!"
    mc "Neyse sakin kalmakta fayda var."

    mc "Fakat yanımda hiçbir şey yok."

    mc "Her zamanki gibi beş parasızım."

    mc "Burası 1800'lerden kalmışa benziyor."

    mc "Param olsa da burada geçersiz olurdu."

    mc "Neyse, en azından belki kolumdaki saat bir işe yarar."

    "" "Ana caddeden uzaklaşıp dar bir sokağa girer."

    "" "Eski taş binalar güneş ışığını keserken etraf giderek sessizleşir."

    "" "Duvar diplerinde tahta kasalar, yerde ise birikmiş yağmur suları vardır."

    "" "Issız bir sokağa varır."
    

    mc "Biraz dolaşmak iyi geldi. Umarım bu sokak beni tekrar ana caddeye çıkarır."
label label_3:
   


    "" "Tam köşeyi döndüğü sırada karşısına şüpheli bir adam çıkar."

    
    show hirsiz:
     xalign 0.5
     yalign 1.0
     zoom 0.55
    with dissolve

    "" "Adam karakterin yolunu keser."

    h "Hey sen! Kolundaki saat güzelmiş, ödünç alabilir miyim?"

    mc "Bana mı diyorsun?"

    h "Başka biri mi var burada? Uzatma da ver şu saati!"

    mc "Dakika bir, gol bir! Gene başladık!"

    mc "Kusura bakma kardeşim, sana bu saati veremem."

    mc "Bu, babamdan kalma son yadigârım."

    "" "Karakterin gözleri dolar."

    h "Demek böyle oynamak istiyorsun."

    "" "Hırsız cebinden hançerini çıkarır ve karaktere doğru bir adım atar."

    mc "Bi kolpa sıkayım dedim o da işe yaramadı. İşte şimdi ayvayı yedim!"

    menu:
        "Hızlıca ana caddeye doğru koşmaya başla.":
            jump kacis

        "Hırsızla dövüşmeye çalış.":
            jump dovus



label kacis:

    mc "Buradan hemen uzaklaşmalıyım!"

    "" "Karakter hızla ana caddeye doğru koşmaya başlar."

    mc "Umarım peşimi bırakır..."

    "" "Tam köşeyi döndüğü sırada aniden birisi karşısına çıkar."

    mc "Hey! Önüne baksana!"

    show eli:
        xalign 0.15
        yalign 1.0
        zoom 0.43
    with dissolve

    e "Bir dakika, sen de kimsin?"

    mc "Şimdi açıklayacak vaktim yok! Peşimde bir hırsız var!"

    e "Hırsız mı?"

    "" "Eli arkasına döner ve yaklaşan hırsızı fark eder."

    show hirsiz:
        xalign 0.85
        yalign 1.0
        zoom 0.55
    with dissolve

    h "Hey! Oradaki ikiniz! Daha işimiz bitmedi!"

    e "Sanırım seninle biraz konuşmamız gerekecek."

    mc "Lütfen bana yardım edeceğini söyle..."

    e "Merak etme. O iş bende."

    "" "Hırsız aniden Eli'ye doğru hamle yapar."

    show eli:
        ease 0.3 xalign 0.42

    show hirsiz:
        ease 0.3 xalign 0.58

    with hpunch

    pause 0.3

    e "Beni bu kadar kolay alt edebileceğini mi sandın?"

    h "Ne?!"

    mc "Vay canına... Bu kız da neyin nesi? Her hamlemi savuşturacak kadar hızlı."

    # Eli hirsiza son darbeyi vurur
    e "Bu kadar oyun yeter!"

    show eli:
        ease 0.3 xalign 0.25
        ease 0.2 xalign 0.42

    show hirsiz:
        ease 0.4 xalign 0.95

    with hpunch

    pause 0.5

    h "Ahh! Tamam, tamam! Pes ediyorum!"

    h "Bir daha karşıma çıkmayın!"

    "" "Hırsız aldığı darbelerin ardından sendeleyerek geri çekilir."

    "" "Yavaşça gözden kaybolur."

    hide hirsiz with dissolve

    pause 0.8

    # Eli ekranin ortasina gelir
    show eli:
        ease 1.2 xalign 0.5

    pause 1.0

    e "Hey, iyi misin?"

    e "Bir yerin incindi mi?"

    mc "Y-yok... İyiyim."

    e "Emin misin? Az önce oldukça korkmuş görünüyordun."

    mc "Evet, sayende iyiyim."

    e "Buna sevindim."

    "" "Ana karakter bir süre Eli'ye bakakalır."

    "" "Kalbi normalden çok daha hızlı atmaya başlar."

    mc "Şey... Sana bir şey sorabilir miyim?"

    e "Tabii, nedir?"

    mc "Benimle evlenir misin?"
    show elisasirmis:
        xalign 0.5
        yalign 1.0
        zoom 0.43
    with dissolve

    pause 1.5

    

    e "..."

    e "Ne?!"

    mc "Benimle... evlenir misin?"

    e "Daha yeni tanıştık!"

    mc "Biliyorum ama..."

    mc "Beni kurtardın, çok cesursun ve..."

    mc "Sanırım sana ilk görüşte aşık oldum."

    e "Sen gerçekten çok tuhaf birisin..."

    pause 1.0

    "" "Eli hafifçe gülümser ve yüzünü başka tarafa çevirir."

    hide elisasirmis
    hide eli

    show elihappy:
     xalign 0.5
     yalign 1.0
     zoom 0.43
    with dissolve

    e "Ama..."

    e "Neden olmasın?"

    mc "Bir dakika... Ciddi misin?!"

    e "Evet. Teklifini kabul ediyorum."

    mc "Gerçekten mi?!"

    e "Ama önce birbirimizi tanımamız gerekecek, değil mi?"

    mc "Elbette!"

    "" "Eli gülümseyerek ana karaktere bakar."

    e "O zaman tanışalım. Ben Eli."

    mc "Ben de..."

    "" "Belki de bu karşılaşma, ikisinin hayatını sonsuza dek değiştirecekti."

    jump evlilik




    return



label dovus:

    mc "Kaçacak değilim!"

    "Karakter yumruklarını sıkarak hırsıza doğru ilerler."

    h "Demek cesursun ha?"

    mc "O saati sana vermeyeceğim!"

    "" "Karakter hırsıza hamle yapar."

    "" "Ancak hırsız beklenmedik bir hızla karşılık verir."

    with vpunch

    mc "Ah! Ne yaptın sen?!"

    h "Sana son bir şans vermiştim."

    "" "Karakter aldığı darbenin etkisiyle geriye çekilir."

    mc "Lanet olsun... Gücüm tükeniyor..."

    h "Bir dahaki sefere karşıma çıkmadan önce iki kere düşün."

    hide hirsiz with dissolve

    "Karakter yavaşça yere çöker."

   
    scene black with fade

    # Ses dosyası hazır olduğunda buraya eklenecek.Buraya ölüm sesi gibi bir şey ekleyeceğiz
    # play sound "audio/game_over.ogg"

    call screen game_over

    jump label_2

    return

screen game_over():

    modal True

    add Solid("#000000")

    text "GAME OVER":
        xalign 0.5
        yalign 0.45
        size 80
        color "#ff0000"
        bold True

    text "Tekrar dene...":
        xalign 0.5
        yalign 0.58
        size 30
        color "#ffffff"
    timer 3.0 action Return()

label evlilik:
    scene bg dugun
    "" "Düğün başlarken Liam hala ne olduğunu kavrayamamıştı"
    mc "Son iki gün hayatımın en hızlı iki günüydü sanırım."
    mc "Benim gibi bir ezik iki gün içinde sıfırdan kraliyetin en güçlü askerinin müstakbel kocasına dönüştü."
    mc "Yaşadıklarım şans olmasa belki de gerçekten kazandığı..."
    mc "Kazanmış ya da kazanmamış olmamın bi anlamı yok. Çünkü şuanda bunlara sahibim zaten."
    show eliwedding:
     xalign 0.5
     yalign 1.0
     zoom 0.43
    with dissolve
    e "Ee hazır mısın"
    mc "Dünden hazırım"
    e "Nasıl bu kadar rahatsın her zaman??? Daha 2 gün önce tanıştığın biriyle evleneceksin şuanda."
    mc "Ne zaman tanıştığımızın bir önemi yok. Sadece seni sevdiğimi biliyorum"
    mc "O gün, o salı günü benim yerimde kim olursa olsun sen yine de yardım edecektin buna eminim..."
    mc "Yani beni özel kılan hiçbir şey yok. Ama aksine ben bunu sevdim. Çünkü benim gibi değersiz bir şeye bile nezaketle yaklaşabilen biri kesinlikle dünyanın en güzelidir"
    jump mutlu_son
                                                                                                                                                                                          
# MUTLU SON EKRANI

label mutlu_son:

    scene black
    with fade

    call screen happy_ending

    return


screen happy_ending():

    modal True

    add "images/mutlu_son.png":
        xysize (config.screen_width, config.screen_height)

    # Ana Menüye Dön butonu
    # Görseldeki yazının üzerine şeffaf tıklama alanı
    button:
        xalign 0.23
        yalign 0.86
        xsize int(config.screen_width * 0.25)
        ysize int(config.screen_height * 0.09)
        background None
        hover_background "#ffffff22"
        action MainMenu(confirm=False)

