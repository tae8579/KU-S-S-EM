from netzob.all import *
import sys
import os
import pydot
from PIL import Image

message_symbols = []

# [1] 프로토콜 추론 기능
def Protocol_Inference(file_path):
    print("[#] IN&S PROTOCOL INFERENCE PROGRAM")
    print("[>] 파일 " + str(file_path) + "에 대한 분석을 수행합니다")
    messages = PCAPImporter.readFile(file_path).values()  # 파일을 PCAPImporter를 통해 읽음

    print("-----------------------------------------------------------------------------------------------------------------")
    print("[1] 프로토콜을 통한 메시지의 종류")
    for message in messages:
        print(message)

    symbol = Symbol(messages=messages)
    Format.splitDelimiter(symbol, ASCII("#"))
    symbols = Format.clusterByKeyField(symbol, symbol.fields[0])

    print("-----------------------------------------------------------------------------------------------------------------")
    # print("[+] Number of symbols after clustering: {0}".format(len(symbols)))
    print("[2] 프로토콜 내 Symbol의 종류:")
    for keyFieldName, s in symbols.items():
        try:
            print("   - " + bytes.fromhex(keyFieldName.decode("utf-8")).decode('utf-8'))
            message_symbols.append(bytes.fromhex(keyFieldName.decode("utf-8")).decode('utf-8'))
        except:
            print("  * {0}".format(keyFieldName))
    print("---------------------------------------------------------------")

    symbol_cnt = 1
    for symbol in symbols.values():
        rels = RelationFinder.findOnSymbol(symbol)
        for rel in rels:
            # Apply first found relationship
            rel = rels[0]
            rel["x_fields"][0].domain = Size(rel["y_fields"], factor=1 / 8.0)

        print("[" + str(symbol_cnt) + "] Packet(Message) Struct")
            
        # recieve row message struct 
        message = symbol._str_debug()
        message = message.replace('Raw', 'Message')
        message = message.replace('Field', 'Attribute')
        message = message.replace('((', 'Range(Min/Max)=')
        message = message.replace('))', '')

        # [1] message_symbol
        message_symbol = message[message.find('Symbol_'):message.find('|')]
        message_symbol = message_symbol.replace('Symbol_','')

        # convert string -> byte
        try:
            byte_message_symbol = str.encode(message_symbol.replace('\n',''))
            byte_message_symbol = bytes.fromhex(byte_message_symbol.decode("utf-8")).decode('utf-8')
        except:
            byte_message_symbol = message_symbol

        # [2] message_offset
        print('[ Message keyword in IN&S inference tool ] ' + byte_message_symbol + message[message.find('|'):])

        symbol_cnt += 1
        print("---------------------------------------------------------------")

    session = Session(messages)
    abstractSession = session.abstract(list(symbols.values()))
    automata = Automata.generateChainedStatesAutomata(abstractSession, list(symbols.values()))

    file_name = os.path.basename(file_path).replace(".pcap","")
    graph_path = os.path.join("FSM", file_name + ".png") # 파일이 저장될 경로
    print("[>] 프로토콜의 동작원리 (FSM:Finite-State Machine) 이미지 저장 및 출력 완료")
    print("[-] 이미지 저장경로 : " + str(graph_path))
    dotcode = automata.generateDotCode() # netzob를 통한 결과를 dotcode 형식으로 받아옴
    graph = pydot.graph_from_dot_data(dotcode)[0] # dotcode 형식을 pydot 라이브러리를 통해 float 형식으로 바꿈
    graph.write_png(graph_path) # float 형식의 결과 이미지를 png 구조로 저장
    image = Image.open(graph_path) # png 파일을 plt 라이브러리를 통해 읽어드림
    image.show() # 이미지를 화면에 출력함


# [1] 메인함수 : 프로그램이 시작되는 지점
if __name__ == '__main__':
    file_path = sys.argv[1]  # 인자를 통해 파일의 경로를 가져옵니다.
    Protocol_Inference(file_path)
