# comic-crawling
時值Netflix上了最新的今際之國的闖關者S2，順手爬了一下某網站的圖文source
* 尋找圖文比較乾淨的網站
* 爬蟲過程中解決困難點
  * 每爬五張會出現一個網站的"勸世圖文"
  * 仔細觀察website element可以發現真正圖文的連結是藏在tag中
  * 由於真正連結是以編號有序地生成，所以在程式中置入正確連結即完成
