import streamlit as st
import requests
import re

ML_ACCESS_TOKEN = "APP_USR-5973721571310127-050510-490a25978992ee35070fd7d9610ce817-3227172442"

st.set_page_config(page_title="Busca Nickname ML", page_icon="🔍")
st.title("🔍 Localizador de Nickname ML")

mlb_input = st.text_input("Cole o MLB do concorrente:", placeholder="Ex: MLB6238793550")

MEU_COOKIE = "Path=/; X-Oracle-BMC-LBS-Route=943a32b1287f53f0d93ff812382d5718bcf904f76bbb6ef2054830b67b985670b6ecb6042865ada2; Path=/; X-Oracle-BMC-LBS-Route=943a32b1287f53f0d93ff812382d5718bcf904f76bbb6ef2054830b67b985670b6ecb6042865ada2; cookieMessage=true; _ga_X2H62NN2WE=GS2.1.s1777921585$o1$g0$t1777921585$j60$l0$h0; _ga=GA1.1.525433419.1777921586; _tt_enable_cookie=1; _ttp=01KQT64WMRZWNMBEVS30713N7T_.tt.2; _fbp=fb.2.1777921586106.411424129117368442; ttcsid_CTE7GPRC77U1739SGEHG=1777921585821::lynGqlBL75HoXvWjurwK.1.1777921595853.1; ttcsid_CTE7FJJC77UEOVFAIGE0=1777921585835::LmEMLccFoYE3QSG6Fvcd.1.1777921595907.1; ttcsid=1777921585825::B5Cg7g49qyLSBhfbbwQs.1.1777921595906.0::1.-775.57::0.0.0.0::19201.34.72; _gcl_au=1.1.1558016399.1777921586.1105550023.1777927910.1777927910; _ga_X4GFCYMMQN=GS2.1.s1777927909$o1$g1$t1777928382$j60$l0$h154951052; PHPSESSID=837a83a4839397addab9766ec8966746; Path=/; X-Oracle-BMC-LBS-Route=943a32b1287f53f0d93ff812382d5718bcf904f76bbb6ef2054830b67b985670b6ecb6042865ada2"

if st.button("Consultar"):
    if mlb_input:
        mlb_limpo = mlb_input.strip()
        headers = {
            "Cookie": MEU_COOKIE,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        try:
            url_sdp = f"https://app.shoppingdeprecos.com.br/produtos/item/{mlb_limpo}"
            res_sdp = requests.get(url_sdp, headers=headers)
            
            if "seller_id" in res_sdp.text:
                match = re.search(r'"seller_id":\s*(\d+)', res_sdp.text)
                
                if match:
                    seller_id = match.group(1)
                    
                    url_ml = f"https://api.mercadolibre.com/users/{seller_id}"
                    params = {"access_token": ML_ACCESS_TOKEN}
                    res_ml = requests.get(url_ml, params=params).json()
                    
                    nickname = res_ml.get("nickname")
                    
                    if nickname:
                        st.success(f"✅ Nickname encontrado: **{nickname}**")
                        st.info(f"Seller ID: {seller_id}")
                        
                        st.write("Clique abaixo para copiar o apelido:")
                        st.code(nickname) 
                    else:
                        st.warning("ID capturado, mas a API do ML não retornou um Nickname público.")
                        with st.expander("Ver resposta da API do ML"):
                            st.json(res_ml) 
                else:
                    st.error("Não foi possível localizar o número do Seller ID no código da página.")
            else:
                st.error("Acesso negado ao Shopping de Preços. O Cookie expirou.")
        except Exception as e:
            st.error(f"Erro na integração: {e}")
