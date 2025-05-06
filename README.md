# Autogen Agent Framework (V1 - Single Agent)

Bu proje, **Autogen** kütüphanesi kullanılarak oluşturulmuş **basit bir agent projesidir**. Şu anda **tek agent** oluşturulmuş, temeller atılmış, sağlam bir başlangıç yapılmıştır; ilerleyen aşamalarda **çoklu agent (multi-agent) senaryoları** ve daha gelişmiş özellikler eklenecektir.

---

## Özellikler

- ✅ **Tek agent yapısı (şu an aktif)**
- ✅ **Gemini & Ollama desteği**
- ✅ **Kolay yapılandırma (.env kullanımı)**
- 🔜 **Multi-agent desteği (v2’de eklenecek)**
- 🔜 **Docker desteği (v3’de planlanıyor)**

---

## Kurulum

1 **Projeyi klonla**

```bash
git clone https://github.com/Kaangml/autogen_agent/.git
cd autogen_agent
```

2 **Ortam oluştur ve bağımlılıkları yükle:**

```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```
3 **.env dosyasını hazırla:**
```bash
#.env
OLLAMA_API_BASE=http://localhost:11434/
GEMINI_API_KEY=YourGeminiAPIKeyHere
```
---
## Kullanım
main.py dosyası, agent’ı başlatır ve temel bir soru sorar.

**Çalıştırmak için:**
```bash
cd autogen_agent
python main.py
```
---
## Proje Yapısı

```bash
├── agents/
│   └── basic_agent.py
├── config/
│   ├── LLM_CONFIG.py
│   └── .env.example
├── main.py
├── requirements.txt
└── README.md
```
