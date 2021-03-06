import CymonCrawler
import VirusTotalValidater
import AVcrawler
import datetime


def crawl(delta_time=1):
    # crawlCymon(delta_time)
    crawAlienVault()
    validateAll()
    
    
def crawlCymon(delta_time):
    cymondelta = min(4, 1 + delta_time)
    CymonCrawler.crawl(range(1,), ['malware'], ['ip', 'domain'])    

def crawAlienVault():    
    AVcrawler.crawl()    
    
def validateAll():
    VirusTotalValidater.validateAll()    
    
crawl()
