from pyvogue import Transaction


s = Transaction()


params = {'v_merchant_id':'demo',
          'memo':'testing',
          'total':'1200'
            }

t = s.paylink(params)

print(t.text)

#https://voguepay.com/pay/bnlink/1467199318-x0
