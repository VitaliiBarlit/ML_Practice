import matplotlib.pyplot as plt
import numpy as np
import time

for kk in range(3):
    test_list = []
    
    
    for n in range(1000,11000,1000):
        x = np.array([[row for row in range(n)] for col in range(n)])
        #y = np.array([[row for row in range(n)] for col in range(n)])
        
        start = time.time()
        np.dot(x,x)
        t = time.time() - start
        test_list.append(time.time() - start)
        
        print('End: {}, time: {}'.format(n, t))
    
    
    X = [i for i in range(len(test_list))]

    with plt.style.context('bmh'):
        fig, ax = plt.subplots()
    
    
        test = ax.bar(X,
                      test_list,
                      width = 0.5,
                      edgecolor='red')
        ax.plot(test_list,'y--')
        ax.set_ylabel('Time, sec')
        ax.set_xlabel('Matrix size, MxM')
        ax.set_title('Matrix calculation time with numpy')
        ax.set_xticks(X)
        ax.set_ylim(0,2600)
        ax.set_xticklabels([i for i in range(1000,11000,1000)])
        ax.bar_label(test, padding=3,labels=['%.1f' % i for i in test_list])
        plt.savefig('plot{}.jpeg'.format(kk), dpi=300)
        plt.show()
    print('End turn: {}'.format(kk))
    
    
    '''
    End: 1000, time: 0.9892232418060303
    End: 2000, time: 10.598870515823364
    End: 3000, time: 34.88852858543396
    End: 4000, time: 109.62109637260437
    End: 5000, time: 179.50116634368896
    End: 6000, time: 364.8732559680939
    End: 7000, time: 544.3221867084503
    End: 8000, time: 1255.395488500595
    End: 9000, time: 1325.6269969940186
    End: 10000, time: 2095.555953979492
    End turn: 0
    End: 1000, time: 0.8795490264892578
    End: 2000, time: 24.429736852645874
    End: 3000, time: 69.49879169464111
    End: 4000, time: 211.71369314193726
    End: 5000, time: 374.1087865829468
    End: 6000, time: 366.87675857543945
    End: 7000, time: 538.9278130531311
    End: 8000, time: 1238.5847034454346
    End: 9000, time: 1984.7112655639648
    End: 10000, time: 2663.071258544922
    End turn: 1
    End: 1000, time: 0.858710765838623
    End: 2000, time: 10.073566198348999
    End: 3000, time: 33.95896029472351
    End: 4000, time: 110.10205173492432
    End: 5000, time: 181.9897975921631
    End: 6000, time: 365.61194372177124
    End: 7000, time: 545.5579829216003
    End: 8000, time: 1239.6739373207092
    End: 9000, time: 1288.6629450321198
    End: 10000, time: 2306.2036731243134
    End turn: 2
    '''