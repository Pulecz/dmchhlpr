# coding: utf-8
import json

# just defined defs, not used
d15='.art, .click, .club, .com, .eu, .fans, .futbol, .in, .link, .net, .nl, .observer, .one, .org, .pictures, .pl, .pm, .re, .rocks, .tel, .top, .wf, .xyz'.split(', ')
d30='.africa, .agency, .airforce, .app, .army, .associates, .auction, .band, .bargains, .beer, .bet, .bid, .bike, .blog, .blue, .boston, .boutique, .builders, .business, .bz, .cab, .cafe, .capetown, .cards, .care, .casa, .cash, .cat, .catering, .cc, .center, .ch, .chat, .cheap, .church, .city, .clothing, .cloud, .co, .coffee, .cologne, .community, .company, .computer, .construction, .consulting, .contractors, .cooking, .cool, .country, .cricket, .cx, .cymru, .dance, .date, .deals, .democrat, .desi, .dev, .digital, .direct, .directory, .discount, .domains, .download, .durban, .earth, .education, .email, .engineer, .enterprises, .equipment, .estate, .events, .exchange, .exposed, .express, .fail, .faith, .family, .farm, .fashion, .fi, .fish, .fishing, .fit, .fitness, .florist, .football, .forsale, .foundation, .fr, .fun, .fyi, .gallery, .games, .garden, .gift, .gifts, .gives, .gmbh, .graphics, .gratis, .gripe, .group, .guide, .haus, .horse, .house, .how, .immo, .immobilien, .industries, .info, .ink, .institute, .international, .irish, .ist, .istanbul, .it, .jetzt, .joburg, .kaufen, .kim, .land, .li, .life, .lighting, .limited, .live, .llc, .loan, .lol, .love, .ltd, .management, .market, .marketing, .mba, .me, .media, .men, .miami, .mobi, .moda, .moe, .money, .nagoya, .navy, .network, .news, .ninja, .nu, .nz, .online, .parts, .party, .pet, .photo, .photography, .photos, .pink, .plus, .productions, .promo, .properties, .pub, .pw, .racing, .red, .rehab, .reisen, .rentals, .repair, .report, .republican, .review, .reviews, .rip, .rodeo, .rs, .run, .sale, .sarl, .school, .schule, .science, .se, .services, .shiksha, .shop, .shopping, .show, .si, .singles, .site, .sk, .soccer, .social, .software, .solutions, .soy, .space, .stream, .studio, .study, .style, .supplies, .supply, .support, .surf, .systems, .team, .technology, .tf, .tips, .today, .tokyo, .tools, .town, .trade, .training, .tube, .tw, .uno, .vacations, .vet, .vg, .video, .vip, .vision, .vodka, .wales, .watch, .webcam, .website, .wedding, .wiki, .win, .works, .world, .ws, .wtf, .yoga, .yokohama, .yt, .zone'.split(', ')
d45='.ac, .apartments, .attorney, .bingo, .black, .buzz, .camera, .camp, .capital, .careers, .charity, .claims, .cleaning, .clinic, .coach, .codes, .condos, .coupons, .courses, .cruises, .dating, .delivery, .dental, .dentist, .design, .diamonds, .dog, .engineering, .expert, .finance, .financial, .flights, .fund, .furniture, .glass, .golf, .gs, .guru, .gy, .healthcare, .hockey, .holdings, .holiday, .hospital, .insure, .io, .jewelry, .kitchen, .kiwi, .la, .lawyer, .lc, .lease, .legal, .lgbt, .limo, .london, .ma, .maison, .memorial, .menu, .mom, .mortgage, .ms, .partners, .pizza, .plumbing, .poker, .ps, .qa, .recipes, .rest, .restaurant, .salon, .shoes, .ski, .solar, .st, .store, .surgery, .sx, .tax, .taxi, .tech, .tennis, .theater, .tienda, .tours, .toys, .tv, .university, .vc, .ventures, .viajes, .villas, .vin, .vlaanderen, .voyage, .wine'.split(', ')
d60='.amsterdam, .archi, .bar, .bio, .build, .college, .do, .fo, .frl, .gd, .gl, .global, .green, .health, .is, .mn, .organic, .pe, .ph, .press, .rent, .sb, .sh, .so, .to, .vegas, .vote, .voto, .wien'.split(', ')
d75='.credit, .energy, .fm, .gold, .hn, .investments, .loans, .mu, .realestate, .reise, .tires'.split(', ')

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
    wanted_top_domains = d15
    pit = load_json('popular_ud_words.json')
    with open('czech_words.txt') as io_wrap:
        czech_words = io_wrap.read()

    search(czech_words,pit)
