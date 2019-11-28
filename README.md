## Communication Deadlines 

Countdown timers to keep track of a bunch of CCF-A,B,C communication conference deadlines.

## Adding/updating a conference

This project is fork from [AIdeadline](https://github.com/abhshkdz/ai-deadlines/)
I write the conference and journal spider based bs4 requests (python3).
The website is built by the light web framework flask.
To keep things minimal, I'm only looking to CCF-A,B,C conferences in communication as per [www.myhuiban.com][6]. Feel free to maintain a separate fork if you don't see your sub-field or conference of interest listed.

To add or update information:
- Fork the repository
- Update `static/conference_list.txt`
- Run conference_spider.py regularly to update meeting information.
- If you want to show the journal info in the website or show other classification label, try to update the front page all.html and single.html
- Send a pull request

## other useful listings
- [comdeadline.com][1] by @leeruibin
- [aideadlin.es][2] by @abhshkdz.
- [geodeadlin.es][3] by @LukasMosser
- [neuro-deadlines][4] by @tbryn
- [ai-challenge-deadlines][5] by @dieg0as
- [CV-oriented ai-deadlines (with an emphasis on medical images)][8] by @duducheng
- [es-deadlines (Embedded Systems, Computer Architecture, and Cyber-physical Systems)][9] by @AlexVonB and @k0nze
- [2019-2020 International Conferences in AI, CV, DM, NLP and Robotics][10] by @JackieTseng

## License

[MIT][1]

[1]: http://www.comdeadline.com/
[2]: http://aideadlin.es/
[3]: http://geodeadlin.es/
[4]: https://github.com/tbryn/neuro-deadlines
[5]: https://github.com/dieg0as/ai-challenge-deadlines
[6]: http://www.conferenceranks.com/#
[8]: https://creedai.github.io/ai-deadlines/
[9]: https://ekut-es.github.io/es-deadlines/
[10]: https://jackietseng.github.io/conference_call_for_paper/conferences.html
