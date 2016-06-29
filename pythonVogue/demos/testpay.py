import transaction

trx = Transaction()

params = {'v_merchant_id':'demo',
          'memo':'testing',
          'total':'1200'
            }

t = trx.paylink(params)

print(t.text)
