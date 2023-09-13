import mouse_action
import utils

def three_drag():
    #不同分辨率屏幕不一样
    locations= [[(400,280),(660,370) ],[(720,280),(980,370) ] ,[(400,450),(660,540) ] ]
    #3个必须一样大
    ans_box = [(1360,315),(1360,540)]
    
    data = {}
    for i in range(3):
        img = ImageGrab.grab(bbox=(locations[i][0][0], locations[i][0][1], locations[i][1][0],locations[i][1][1]))  # bbox 定义左、上、右和下像素的4元组
        img.save(f'temp{i}.jpg')
        img = cv2.imread(f'temp{i}.jpg')
        data[f'base64_{i}']=image_to_base64(img)  
        
    url3 =  "https://animated-orbit-rwxpw7p6v6v3p6qw-5000.app.github.dev/ocr3"
    response = requests.post(url3, json = json.loads(json.dumps(data)), headers=headers)
    if response.status_code == 200:
        results = json.loads(str(response.content, 'utf-8')) 
        scores = results['result'] 
        poss = [ obj['pos'] for obj in scores]
        negs= [ obj['neg'] for obj in scores]
        texts = [ obj['text'] for obj in scores]
        
        true_scores = [ [ a - 2 * b,i] for i,a,b in zip(range(len(poss)),poss,negs) ] 
        true_scores.sort(key=lambda x:-x[0])
        
        best = true_scores[0][1]
        worst = true_scores[-1][1]
        centerx = (locations[best][0][0]+locations[best][1][0])//2
        centery = (locations[best][0][1]+locations[best][1][1])//2
        mouse_drag((centerx,centery) ,ans_box[0])
        #print(f'从{centerx},{centery}拖到{ans_box[0]}')
        centerx = (locations[worst][0][0]+locations[worst][1][0])//2
        centery = (locations[worst][0][1]+locations[worst][1][1])//2
        mouse_drag((centerx,centery) ,ans_box[1])
        #print(f'从{centerx},{centery}拖到{ans_box[1]}')
        print(results)
        print(f'最适合选{best},得分{true_scores[0][0]},最不适合选{worst},得分{true_scores[-1][0]}')
        
        with open('cepin3.log','a') as fp:
            for i in range(len(poss)):
                fp.write(f"{texts[i]}\n")
                fp.write(f"{poss[i]}\n{negs[i]}\n")
        
        return True
    else:
        print('failed')
        return False

 

def 三个拖来拖去(epoch=98): 
    time.sleep(20)#你要在这段时间跳过前面的示例
    for _ in range(epoch): 
        t0 = time.time()
        succ = three_drag()
        print(f'耗时{time.time()-t0}')
        if not succ:
            break
        time.sleep(9)
 

if __name__=="__main__":
    三个拖来拖去()
