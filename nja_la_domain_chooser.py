# coding: utf-8
import json

# just defined defs, not used
d15='.be, .click, .club, .com, .eu, .in, .link, .net, .nl, .org'.split(', ')
d30='.agency, .band, .bet, .bid, .blog, .blue, .business, .bz, .capetown, .cat, .center, .ch, .city, .co, .cologne, .company, .cymru, .cz, .dance, .desi, .directory, .durban, .earth, .education, .email, .equipment, .exposed, .family, .football, .fun, .futbol, .fyi, .gallery, .games, .gift, .graphics, .gratis, .group, .im, .info, .ink, .institute, .international, .irish, .ist, .istanbul, .jetzt, .joburg, .kim, .koeln, .li, .lighting, .live, .ltd, .management, .me, .miami, .mobi, .moda, .moe, .nagoya, .network, .news, .ninja, .nu, .nz, .online, .pet, .photography, .photos, .pictures, .pink, .pl, .promo, .red, .reisen, .report, .reviews, .rip, .rocks, .run, .schule, .se, .shiksha, .si, .soccer, .solutions, .soy, .studio, .supplies, .supply, .support, .systems, .technology, .tel, .tips, .tk, .today, .tokyo, .trade, .tw, .video, .vip, .wales, .webcam, .website, .wiki, .ws, .yokohama'.split(', ')
d45='.airforce, .army, .associates, .attorney, .auction, .bargains, .beer, .bike, .black, .boutique, .brussels, .builders, .buzz, .cab, .cafe, .cards, .care, .casa, .cash, .catering, .cc, .chat, .cheap, .church, .clothing, .coffee, .community, .computer, .construction, .consulting, .contractors, .cooking, .cool, .country, .courses, .cricket, .date, .deals, .democrat, .dentist, .digital, .direct, .discount, .domains, .download, .engineer, .enterprises, .estate, .events, .exchange, .express, .fail, .faith, .farm, .fashion, .feedback, .fish, .fishing, .fit, .fitness, .florist, .forsale, .foundation, .garden, .gifts, .gives, .gmbh, .gripe, .gs, .guide, .guru, .gy, .haus, .horse, .house, .immo, .immobilien, .industries, .io, .kaufen, .kiwi, .kr, .la, .land, .lawyer, .lc, .lgbt, .life, .limited, .loan, .lol, .london, .love, .market, .marketing, .mba, .media, .men, .menu, .mom, .money, .mortgage, .ms, .navy, .parts, .party, .photo, .place, .plus, .poker, .productions, .properties, .pub, .racing, .rehab, .rentals, .repair, .republican, .rest, .review, .rio, .rodeo, .ruhr, .sale, .sarl, .school, .science, .services, .sh, .shop, .shopping, .show, .singles, .site, .ski, .social, .software, .st, .stream, .study, .style, .surf, .sx, .team, .to, .tools, .town, .training, .tube, .tv, .uno, .vacations, .vc, .vet, .vision, .vlaanderen, .vodka, .watch, .wedding, .wien, .win, .works, .world, .wtf, .yoga, .zone'.split(', ')
d60='.alsace, .apartments, .bingo, .camera, .camp, .capital, .careers, .claims, .cleaning, .clinic, .coach, .codes, .condos, .coupons, .cruises, .dating, .delivery, .dental, .design, .diamonds, .dog, .engineering, .expert, .finance, .financial, .flights, .frl, .fund, .furniture, .gd, .gl, .glass, .golf, .hamburg, .healthcare, .hockey, .holdings, .holiday, .hospital, .insure, .jewelry, .kitchen, .lease, .legal, .limo, .maison, .memorial, .mn, .paris, .partners, .ph, .pizza, .plumbing, .qa, .recipes, .restaurant, .salon, .shoes, .solar, .store, .surgery, .tax, .taxi, .tech, .tennis, .theater, .tienda, .tours, .toys, .university, .vegas, .ventures, .viajes, .villas, .vin, .voyage, .wine'.split(', ')
d75='.archi, .bar, .barcelona, .bio, .build, .cd, .college, .ec, .fans, .fm, .global, .green, .hn, .is, .ma, .mu, .organic, .pe, .press, .rent, .so, .vote, .voto'.split(', ')

domain_map = [
    d15,
    d30,
    d45,
    d60,
    d75
]

def load_json(json_file):
    with open(json_file) as io_wrap:
        return json.loads(io_wrap.read())
    
def find_in_dict_on_second_level(target_dict, what):
    " made for popular_ud_words.json format, will print words ending with searched string"
    for starting_letter, words in target_dict.items():
        for word in words:
            #second level
            if word.endswith(what):
                print('UD:', word)

def search(words,pit):
    """print stuff and search through domains without first character
    see how wanted_top_domains are defined"""
    for domain in wanted_top_domains:
        print(12 * '*', 'for', domain[1:])
        if domain.startswith('.'):
            find_in_dict_on_second_level(pit, domain[1:])
            for word in czech_words.split('\n'):
                if word.endswith(domain[1:]):
                    print(word)


if __name__ == '__main__':
    wanted_top_domains = ['.be', '.cz', '.eu', '.in', '.nl', '.la']
    pit = load_json('popular_ud_words.json')
    with open('czech_words.txt') as io_wrap:
        czech_words = io_wrap.read()

    search(czech_words,pit)
