goodwords = ["engrossing", "intriguing", "quirky", "wonderful", "satisfying", "amusing", "spirit", "hilarious", "fresh", "perfect", "enjoy", "clever", "special", "terrific", "fine", "star", "beautifully", "pretty", "strong", "smart", "touching", "intelligent", "art", "beautiful", "charming", "engaging", "charm", "powerful", "sweet", "interesting", "enjoyable", "emotional", "fascinating", "better", "compelling", "humor", "heart", "entertaining", "great", "fun", "love", "best", "funny", "good"]
badwords = ["awful", "horrible", "pretentious", "lacks", "flat", "fails", "mess", "problem", "lack", "lacking", "predictable", "poorly", "poor", "least", "worst", "boring", "silly", "old", "dull", "bad"]

def main(sample):
    temp = ''
    goodcounter = 0
    badcounter = 0
    for letter in sample:
        if letter != ' ':
            temp = temp + letter
        elif letter == ".":
            pass
        else:
            if temp in goodwords:
                goodcounter += 1
            elif temp in badwords:
                badcounter += 3
            temp = ''
    if goodcounter > badcounter:
        print("They thought the show was good")
        print(goodcounter)
        print(badcounter)
    elif badcounter > goodcounter:
        print("They thought the show was bad")
        print(goodcounter)
        print(badcounter)
    else:
        print("They thought the show was just ok")
        print(goodcounter)
        print(badcounter)
                
if __name__ == "__main__":
    main("And just like that, DC’s new streaming service continues its success run with Swamp Thing, arguably their best live-action adaptation on the service. Not even the shows cancelation due to budgeting errors can hold back the greatness of the green. From the opening minutes, its clear everyone associated with the project poured their undying passions into every minute. The cast does an exceptional job in their portrayals, especially Reed and Mears/Bean’s chemistry. It’s a simple concept pushed to a higher caliber. Huge props to the crew for crafting such gorgeous VFX for a television sized series. Production alone can be enough to attract.  The greatest aspect, however, is the cleverly complex overarching narrative. The show’s ability to craft such a compelling world that plays beautifully off different genres effortlessly breeds new meaning to Sci-Fi Horror. While it's not something that makes or breaks the show, there’s occasionally odd voice over for Swamp Thing. There seems to be a minor lack of consistency through the second half of the season, but it can be easily ignored thanks to the more interesting aspect of the story. But with the cancellation of the show, pacing issues are brought up, some present throughout the season with the major one present in the final episode because of the original 13-episode story being condensed to 10 episodes. Swamp Thing allows DC Universe to represent an entirely new frontier of entertainment for the service—Horror—in the most natural and organic way possible; its combination of scientific discovery and small-town drama thrown into the horror mix keeps every aspect of the show engaging to an endless amount. While there are issues present, the show keeps the momentum without its issues even being noticeable unless nitpicked. The show may not return for some time, but it’s clear there were things in motion for future seasons. Whatever the future holds, DC has reached another memorable milestone.")
    main("Ok, here is my final verdict on Swamp Thing. Spoiler free. Having spent 450 minutes watching season 1 in it's entirety, I've given this show far more time than it deserved. I spent the first couple of episodes clinging onto the desperate hope that it would improve. If anything, it's shortcomings just became even more exaggerated as time went on. Main character's back stories and motovations were desperately shallow and one dimensional. Almost every box in the box of clichés was ticked. In the graphic novels, Swamp Thing himself had do let go of his humanity in order to truly become the hero that he is. He had to come to terms with the fact that the man he once was is never coming back, and move on with his new found reason for existence. This is the ONLY thing they touch on that is relatively similar, albeit in a very weak and half-arsed fashion. Woodrue and Sunderland both make an appearance but their back stories are wildly different from those of the graphic novels which I know and love. They are charicatures of themselves, and just serve merely as a means of crowbar-ing known adversaries into the series. The addition of the blue devil is one of the most poorly executed tie-ins I think I've ever seen committed to moving image. Absolutely shocking.")
    main("A lot of things went right in this series, and a lot of things also went wrong. The show gets confusing for a those who don't have any back knowledge of the characters. Some characters appear out of nowhere and are important all of a sudden, like Madame Xanadu. Some are just introduced to fit into the story, kind of squeezed in, like Sussy Coyle's uncle. The actors are great and amazing. Their acting is top notch, but the story line is a but confusing. I'm not really digging the horror vibe the movie has. Especially when the people hunting others have no backstory. We're just left with lines in-between to kinda guess or fill in the gap. It's not done the right way. The show definitely creates a great level of suspense and it kept me on my toes. I kept coming for more. Great show in general. Sad thing it got cancelled.")
    main("How not to make a comic TV series. This has more in common with the 60's Batman TV series. Clunky plotting and a camp delivery with dialogue so bad my cat vomited. It's not helped by Amazon's platform which makes everything look like home video. Someone spotted this and pulled the plug. Avoid.")
    main("Swamp Thing is a great show. Those who love mystery/horror will love it. It sets the mood and tone at the very first minutes of the pilot and sucks you in the story as you move along. The pilot is very satisfying and checks all the boxes, as it is very hard to pull off a superhero show with horror. The characters are great and the acting is very good all across the board. The cinematography is beautiful and on the level of a feature film. If you want something new and fresh this is the show to watch. 9/10.")
