
import requests
import json
import urllib



class Transaction():


    def getall(self,trx,res,decode_content=False):
        """
        Gets all your transactions
        
        args:
        trx -- the transaction id to be fetched 
        res -- the response type expected : json or xml 
        """
        url = "https://voguepay.com/?v_transaction_id="+str(trx)+"&type="+str(res)
    
        if ( decode_content ):
         dec = self.__parse_json(requests.get(url).text)
         return (dec)
        else:
         return requests.get(url).text


    def paylink(self,param):
        
        """
        Generate a one time payment link from params
        
        args:
        param -- a dictionary of payment params 

        e.g
        params = {'v_merchant_id':'14307-23682',
                  'memo':'testing',
                   'total':'1200'
                     }
        
        """
      
        urlg = "https://voguepay.com/?p=linkToken&"+urllib.urlencode(param)
        return requests.get(urlg)


    def __parse_json(self, response_obj):
        """
        This function takes in  json response sent back by the
        server 
        Returns a python dictionary of status, email, amount,memo etc
        """
        data = json.loads(response_obj)    
        return data



