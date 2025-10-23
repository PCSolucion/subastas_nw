
# Modificar el código para usar Pesetas en lugar de Euros

html_code = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subasta Twitch - Liiukiin</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e0836 0%, #2d1850 100%);
            color: #fff;
            min-height: 100vh;
            padding: 20px;
        }
        .header {
            text-align: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 2.5em;
            color: #9147ff;
            text-shadow: 0 0 20px rgba(145, 71, 255, 0.5);
        }
        .connection-status {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(0, 0, 0, 0.4);
            padding: 10px 20px;
            border-radius: 25px;
            margin-top: 15px;
        }
        .status-indicator {
            width: 15px;
            height: 15px;
            border-radius: 50%;
            background: #ff4444;
            animation: pulse 2s infinite;
        }
        .status-indicator.connected {
            background: #44ff44;
            animation: none;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .connect-btn {
            background: #9147ff;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s;
            margin: 10px 5px;
        }
        .connect-btn:hover {
            background: #7c3aed;
            transform: scale(1.05);
        }
        .admin-btn {
            background: #ff6b00;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s;
            margin: 10px 5px;
        }
        .admin-btn:hover {
            background: #e55d00;
            transform: scale(1.05);
        }
        .container {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }
        .auction-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .auction-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(145, 71, 255, 0.3);
            transition: all 0.3s;
            position: relative;
        }
        .auction-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(145, 71, 255, 0.4);
        }
        .auction-card.active {
            border-color: #9147ff;
            box-shadow: 0 0 20px rgba(145, 71, 255, 0.5);
        }
        .edit-icon {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255, 107, 0, 0.8);
            border: none;
            color: white;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 18px;
            transition: all 0.3s;
            z-index: 10;
        }
        .edit-icon:hover {
            background: #ff6b00;
            transform: scale(1.1);
        }
        .item-image-container {
            width: 100%;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            margin: 10px 0;
            overflow: hidden;
        }
        .item-image {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            border-radius: 10px;
        }
        .item-emoji {
            font-size: 4em;
            text-align: center;
            margin: 10px 0;
        }
        .item-title {
            font-size: 1.5em;
            margin: 10px 0;
            color: #fff;
        }
        .item-price {
            font-size: 1.8em;
            color: #44ff44;
            font-weight: bold;
            margin: 10px 0;
        }
        .item-description {
            color: #ccc;
            margin: 10px 0;
            font-size: 0.9em;
        }
        .timer {
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-size: 1.5em;
            margin: 10px 0;
        }
        .timer.urgent {
            background: rgba(255, 0, 0, 0.3);
            animation: blink 1s infinite;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        .auction-controls {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        .btn {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .btn-start {
            background: #44ff44;
            color: #000;
        }
        .btn-stop {
            background: #ff4444;
            color: #fff;
        }
        .btn:hover {
            transform: scale(1.05);
        }
        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: scale(1);
        }
        .bids-panel {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(145, 71, 255, 0.3);
            max-height: 80vh;
            overflow-y: auto;
        }
        .bids-panel h2 {
            color: #9147ff;
            margin-bottom: 20px;
            text-align: center;
        }
        .bid-item {
            background: rgba(255, 255, 255, 0.05);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            border-left: 4px solid #9147ff;
            animation: slideIn 0.3s ease-out;
        }
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        .bid-item.winning {
            background: rgba(68, 255, 68, 0.1);
            border-left-color: #44ff44;
        }
        .bid-user {
            font-weight: bold;
            color: #9147ff;
            font-size: 1.1em;
        }
        .bid-amount {
            font-size: 1.5em;
            color: #44ff44;
            font-weight: bold;
        }
        .bid-time {
            color: #999;
            font-size: 0.8em;
            margin-top: 5px;
        }
        .no-bids {
            text-align: center;
            color: #999;
            padding: 40px;
            font-style: italic;
        }
        .chat-log {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            padding: 10px;
            max-height: 200px;
            overflow-y: auto;
            font-family: monospace;
            font-size: 0.85em;
            margin-top: 10px;
        }
        .chat-message {
            padding: 3px 5px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            word-wrap: break-word;
        }
        .chat-message.success { color: #44ff44; }
        .chat-message.error { color: #ff4444; }
        .chat-message.info { color: #44aaff; }
        
        /* Modal de edición */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(5px);
        }
        .modal.show {
            display: flex;
            justify-content: center;
            align-items: center;
            animation: fadeIn 0.3s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .modal-content {
            background: linear-gradient(135deg, #2d1850 0%, #1e0836 100%);
            padding: 30px;
            border-radius: 15px;
            max-width: 600px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            border: 2px solid #9147ff;
            box-shadow: 0 0 30px rgba(145, 71, 255, 0.5);
            animation: slideDown 0.3s;
        }
        @keyframes slideDown {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .modal-header h2 {
            color: #9147ff;
            font-size: 1.8em;
        }
        .close-btn {
            background: #ff4444;
            border: none;
            color: white;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
            font-weight: bold;
            transition: all 0.3s;
        }
        .close-btn:hover {
            background: #cc0000;
            transform: rotate(90deg);
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            color: #9147ff;
            font-weight: bold;
            margin-bottom: 8px;
            font-size: 1.1em;
        }
        .form-group input[type="text"],
        .form-group input[type="number"],
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid rgba(145, 71, 255, 0.3);
            border-radius: 8px;
            background: rgba(0, 0, 0, 0.3);
            color: white;
            font-size: 16px;
            transition: all 0.3s;
        }
        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #9147ff;
            box-shadow: 0 0 10px rgba(145, 71, 255, 0.3);
        }
        .form-group textarea {
            resize: vertical;
            min-height: 80px;
        }
        .image-upload {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .image-preview-container {
            width: 100%;
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            border: 2px solid rgba(145, 71, 255, 0.3);
            overflow: hidden;
        }
        .image-preview {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            border-radius: 10px;
        }
        .upload-btn {
            background: #9147ff;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .upload-btn:hover {
            background: #7c3aed;
            transform: scale(1.02);
        }
        .save-btn {
            width: 100%;
            background: #44ff44;
            color: #000;
            padding: 15px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            font-size: 18px;
            margin-top: 20px;
            transition: all 0.3s;
        }
        .save-btn:hover {
            background: #33dd33;
            transform: scale(1.02);
        }
        .remove-image-btn {
            background: #ff4444;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .remove-image-btn:hover {
            background: #cc0000;
        }
        
        @media (max-width: 768px) {
            .container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏆 Subasta en Vivo - Liiukiin 🏆</h1>
        <div class="connection-status">
            <div class="status-indicator" id="statusIndicator"></div>
            <span id="statusText">Desconectado de Twitch</span>
        </div>
        <br>
        <button class="connect-btn" id="connectBtn">Conectar a Twitch Chat</button>
        <button class="admin-btn" id="adminBtn">⚙️ Administrar Premios</button>
        <div style="margin-top: 10px; font-size: 0.9em; color: #ccc;">
            Formato de puja: <strong style="color: #44ff44;">!300</strong> (escribe en el chat de Twitch)
        </div>
    </div>
    <div class="container">
        <div class="auction-grid" id="auctionGrid"></div>
        <div class="bids-panel">
            <h2>📊 Pujas en Tiempo Real</h2>
            <div id="bidsContainer">
                <div class="no-bids">Esperando pujas...</div>
            </div>
            <div class="chat-log" id="chatLog">
                <strong>📜 Log de Conexión:</strong>
            </div>
        </div>
    </div>

    <!-- Modal de edición -->
    <div id="editModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>✏️ Editar Premio</h2>
                <button class="close-btn" onclick="closeEditModal()">×</button>
            </div>
            <form id="editForm">
                <div class="form-group">
                    <label>📝 Título del Premio</label>
                    <input type="text" id="editTitle" placeholder="Ej: PlayStation 5" required>
                </div>
                <div class="form-group">
                    <label>💰 Precio Inicial (Pesetas)</label>
                    <input type="number" id="editPrice" min="1" placeholder="Ej: 500" required>
                </div>
                <div class="form-group">
                    <label>📄 Descripción</label>
                    <textarea id="editDescription" placeholder="Descripción del premio"></textarea>
                </div>
                <div class="form-group">
                    <label>🖼️ Imagen del Premio</label>
                    <div class="image-upload">
                        <div class="image-preview-container" id="imagePreviewContainer" style="display: none;">
                            <img id="imagePreview" class="image-preview">
                        </div>
                        <input type="file" id="imageInput" accept="image/*" style="display: none;">
                        <button type="button" class="upload-btn" onclick="document.getElementById('imageInput').click()">
                            📁 Seleccionar Imagen desde PC
                        </button>
                        <button type="button" class="remove-image-btn" id="removeImageBtn" style="display: none;" onclick="removeImage()">
                            🗑️ Quitar Imagen
                        </button>
                        <small style="color: #999;">La imagen se verá completa sin recortes. Máximo 5MB</small>
                    </div>
                </div>
                <button type="submit" class="save-btn">💾 Guardar Cambios</button>
            </form>
        </div>
    </div>

    <script>
        const CHANNEL = 'liiukiin';
        const WEBSOCKET_URL = 'wss://irc-ws.chat.twitch.tv:443';
        
        const defaultAuctionItems = [
            { id: 1, title: "Nintendo Switch OLED", emoji: "🎮", startPrice: 250, description: "Consola Nintendo Switch OLED en perfecto estado", image: null },
            { id: 2, title: "iPhone 14 Pro", emoji: "📱", startPrice: 800, description: "iPhone 14 Pro 256GB, color morado", image: null },
            { id: 3, title: "Funko Pop Rare", emoji: "🎯", startPrice: 50, description: "Funko Pop exclusivo edición limitada", image: null },
            { id: 4, title: "Auriculares Gamer", emoji: "🎧", startPrice: 120, description: "Auriculares gaming RGB con micrófono", image: null },
            { id: 5, title: "Tarjeta Gráfica RTX", emoji: "💻", startPrice: 600, description: "NVIDIA RTX 4070 nueva en caja", image: null },
            { id: 6, title: "Camiseta Firmada", emoji: "👕", startPrice: 75, description: "Camiseta firmada por streamer famoso", image: null }
        ];

        let auctionItems = JSON.parse(localStorage.getItem('auctionItems')) || defaultAuctionItems;
        let ws = null, isConnected = false, isAuthenticated = false, activeAuctions = {}, allBids = {}, nickname = '';
        let currentEditingId = null;
        
        const connectBtn = document.getElementById('connectBtn');
        const adminBtn = document.getElementById('adminBtn');
        const statusIndicator = document.getElementById('statusIndicator');
        const statusText = document.getElementById('statusText');
        const auctionGrid = document.getElementById('auctionGrid');
        const bidsContainer = document.getElementById('bidsContainer');
        const chatLog = document.getElementById('chatLog');
        const editModal = document.getElementById('editModal');
        const editForm = document.getElementById('editForm');
        const imageInput = document.getElementById('imageInput');
        const imagePreview = document.getElementById('imagePreview');
        const imagePreviewContainer = document.getElementById('imagePreviewContainer');
        const removeImageBtn = document.getElementById('removeImageBtn');

        function saveAuctionItems() {
            localStorage.setItem('auctionItems', JSON.stringify(auctionItems));
        }

        function openEditModal(id) {
            currentEditingId = id;
            const item = auctionItems.find(i => i.id === id);
            
            document.getElementById('editTitle').value = item.title;
            document.getElementById('editPrice').value = item.startPrice;
            document.getElementById('editDescription').value = item.description || '';
            
            if (item.image) {
                imagePreview.src = item.image;
                imagePreviewContainer.style.display = 'flex';
                removeImageBtn.style.display = 'block';
            } else {
                imagePreviewContainer.style.display = 'none';
                removeImageBtn.style.display = 'none';
            }
            
            editModal.classList.add('show');
        }

        function closeEditModal() {
            editModal.classList.remove('show');
            currentEditingId = null;
            editForm.reset();
            imagePreviewContainer.style.display = 'none';
            removeImageBtn.style.display = 'none';
        }

        imageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                if (file.size > 5 * 1024 * 1024) {
                    alert('La imagen es demasiado grande. Máximo 5MB.');
                    return;
                }
                
                const reader = new FileReader();
                reader.onload = function(event) {
                    imagePreview.src = event.target.result;
                    imagePreviewContainer.style.display = 'flex';
                    removeImageBtn.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });

        function removeImage() {
            imagePreview.src = '';
            imagePreviewContainer.style.display = 'none';
            removeImageBtn.style.display = 'none';
            imageInput.value = '';
        }

        editForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const item = auctionItems.find(i => i.id === currentEditingId);
            item.title = document.getElementById('editTitle').value;
            item.startPrice = parseInt(document.getElementById('editPrice').value);
            item.description = document.getElementById('editDescription').value;
            
            if (imagePreviewContainer.style.display === 'flex') {
                item.image = imagePreview.src;
            } else {
                item.image = null;
            }
            
            saveAuctionItems();
            renderAuctions();
            closeEditModal();
            
            alert('✅ Premio actualizado correctamente!');
        });

        editModal.addEventListener('click', function(e) {
            if (e.target === editModal) {
                closeEditModal();
            }
        });

        adminBtn.addEventListener('click', function() {
            alert('💡 Para editar un premio, haz clic en el botón ✏️ en la esquina superior derecha de cada tarjeta.');
        });

        function connectToTwitch() {
            if (ws && ws.readyState === WebSocket.OPEN) { ws.close(); return; }
            addChatLog('🔄 Iniciando conexión...', 'info');
            try {
                ws = new WebSocket(WEBSOCKET_URL);
                nickname = `justinfan${Math.floor(Math.random() * 100000)}`;
                ws.onopen = () => {
                    addChatLog('✅ WebSocket conectado', 'success');
                    addChatLog(`📤 Enviando autenticación como ${nickname}...`, 'info');
                    ws.send('CAP REQ :twitch.tv/commands twitch.tv/tags\\r\\n');
                    ws.send('PASS oauth:justinfan12345\\r\\n');
                    ws.send(`NICK ${nickname}\\r\\n`);
                };
                ws.onmessage = (event) => {
                    event.data.split('\\r\\n').filter(msg => msg.length > 0).forEach(message => handleIRCMessage(message));
                };
                ws.onerror = (error) => { addChatLog('❌ Error de conexión', 'error'); updateConnectionStatus(false); };
                ws.onclose = (event) => { addChatLog(`⚠️ Conexión cerrada (código: ${event.code})`, 'error'); updateConnectionStatus(false); isAuthenticated = false; };
            } catch (error) { addChatLog('❌ ERROR: ' + error.message, 'error'); updateConnectionStatus(false); }
        }

        function handleIRCMessage(message) {
            console.log('< ' + message);
            if (message.startsWith('PING')) { ws.send(message.replace('PING', 'PONG') + '\\r\\n'); addChatLog('🏓 PONG enviado', 'info'); return; }
            if (message.includes(' 001 ') || message.includes('Welcome, GLHF!')) { addChatLog('✅ Autenticación exitosa!', 'success'); isAuthenticated = true; ws.send(`JOIN #${CHANNEL}\\r\\n`); addChatLog(`📥 Uniéndose al canal #${CHANNEL}...`, 'info'); return; }
            if (message.includes(`JOIN #${CHANNEL}`)) { addChatLog(`✅ Conectado al canal #${CHANNEL}!`, 'success'); updateConnectionStatus(true); return; }
            if (message.includes('Login authentication failed') || message.includes('Improperly formatted auth')) { addChatLog('❌ Error de autenticación', 'error'); updateConnectionStatus(false); if (ws) ws.close(); return; }
            if (message.includes('PRIVMSG')) parsePrivMsg(message);
            if (message.includes('NOTICE')) { const noticeMatch = message.match(/NOTICE.*?:(.+)$/); if (noticeMatch) addChatLog('📢 ' + noticeMatch[1], 'info'); }
        }

        function parsePrivMsg(rawMessage) {
            try {
                const userMatch = rawMessage.match(/:([^!]+)!/);
                const messageMatch = rawMessage.match(/PRIVMSG #[^ ]+ :(.+)$/);
                if (!userMatch || !messageMatch) return;
                const username = userMatch[1];
                const message = messageMatch[1].trim();
                const bidMatch = message.match(/^!(\\d+)$/);
                if (bidMatch) { const amount = parseInt(bidMatch[1]); processBid(username, amount); }
            } catch (error) { console.error('Error parseando PRIVMSG:', error); }
        }

        function processBid(username, amount) {
            const activeAuctionId = Object.keys(activeAuctions).find(id => activeAuctions[id].active);
            if (!activeAuctionId) { addChatLog(`💰 ${username}: ${amount} Pesetas - Sin subasta activa`, 'error'); return; }
            const auction = activeAuctions[activeAuctionId];
            const currentHighest = auction.currentBid || auction.startPrice;
            if (amount <= currentHighest) { addChatLog(`❌ ${username}: ${amount} Pesetas - Muy baja (actual: ${currentHighest} Pesetas)`, 'error'); return; }
            const bid = { username, amount, timestamp: new Date(), auctionId: activeAuctionId };
            if (!allBids[activeAuctionId]) allBids[activeAuctionId] = [];
            allBids[activeAuctionId].push(bid);
            auction.currentBid = amount;
            auction.currentWinner = username;
            auction.bidCount = (auction.bidCount || 0) + 1;
            if (auction.timeLeft < 30) { auction.timeLeft += 10; addChatLog(`⏰ Tiempo extendido +10s`, 'info'); }
            addChatLog(`✅ ${username}: ${amount} Pesetas - NUEVA PUJA LÍDER!`, 'success');
            renderBids(activeAuctionId);
            renderAuctions();
            animateBid(activeAuctionId);
        }

        function animateBid(auctionId) {
            const card = document.querySelector(`[data-auction-id="${auctionId}"]`);
            if (card) { card.style.transform = 'scale(1.05)'; card.style.boxShadow = '0 0 30px rgba(68, 255, 68, 0.6)'; setTimeout(() => { card.style.transform = 'scale(1)'; card.style.boxShadow = ''; }, 300); }
        }

        function updateConnectionStatus(connected) {
            isConnected = connected;
            if (connected) { statusIndicator.classList.add('connected'); statusText.textContent = `Conectado a #${CHANNEL}`; connectBtn.textContent = 'Desconectar'; connectBtn.style.background = '#ff4444'; }
            else { statusIndicator.classList.remove('connected'); statusText.textContent = 'Desconectado'; connectBtn.textContent = 'Conectar a Twitch Chat'; connectBtn.style.background = '#9147ff'; }
        }

        function addChatLog(message, type = '') {
            const msgElement = document.createElement('div');
            msgElement.className = 'chat-message ' + type;
            msgElement.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
            chatLog.appendChild(msgElement);
            chatLog.scrollTop = chatLog.scrollHeight;
            while (chatLog.children.length > 101) chatLog.removeChild(chatLog.children[1]);
        }

        connectBtn.addEventListener('click', () => { if (isConnected) { if (ws) ws.close(); updateConnectionStatus(false); } else connectToTwitch(); });

        function renderAuctions() {
            auctionGrid.innerHTML = '';
            auctionItems.forEach(item => {
                const auction = activeAuctions[item.id] || { active: false, timeLeft: 300, currentBid: item.startPrice, currentWinner: null, bidCount: 0, startPrice: item.startPrice };
                activeAuctions[item.id] = auction;
                const card = document.createElement('div');
                card.className = 'auction-card' + (auction.active ? ' active' : '');
                card.setAttribute('data-auction-id', item.id);
                
                let imageHTML = '';
                if (item.image) {
                    imageHTML = `<div class="item-image-container"><img src="${item.image}" class="item-image" alt="${item.title}"></div>`;
                } else {
                    imageHTML = `<div class="item-emoji">${item.emoji}</div>`;
                }
                
                let timerHTML = '';
                if (auction.active) { 
                    const minutes = Math.floor(auction.timeLeft / 60); 
                    const seconds = auction.timeLeft % 60; 
                    const timerClass = auction.timeLeft < 30 ? 'timer urgent' : 'timer'; 
                    timerHTML = `<div class="${timerClass}">⏱️ ${minutes}:${seconds.toString().padStart(2, '0')}</div>`; 
                }
                
                let winnerHTML = '';
                if (auction.currentWinner) winnerHTML = `<div style="background: rgba(68, 255, 68, 0.2); padding: 10px; border-radius: 8px; margin: 10px 0;"><strong>🏆 Líder:</strong> ${auction.currentWinner}<br><strong>Pujas:</strong> ${auction.bidCount}</div>`;
                
                card.innerHTML = `
                    <button class="edit-icon" onclick="openEditModal(${item.id})">✏️</button>
                    ${imageHTML}
                    <div class="item-title">${item.title}</div>
                    <div class="item-description">${item.description}</div>
                    <div class="item-price">${auction.currentBid} Pesetas</div>
                    ${winnerHTML}
                    ${timerHTML}
                    <div class="auction-controls">
                        <button class="btn btn-start" onclick="startAuction(${item.id})" ${auction.active ? 'disabled' : ''}>
                            ${auction.active ? '🔴 En curso' : '▶️ Iniciar'}
                        </button>
                        <button class="btn btn-stop" onclick="stopAuction(${item.id})" ${!auction.active ? 'disabled' : ''}>
                            ⏹️ Detener
                        </button>
                    </div>
                `;
                auctionGrid.appendChild(card);
            });
        }

        function renderBids(auctionId) {
            const bids = allBids[auctionId] || [];
            if (bids.length === 0) { bidsContainer.innerHTML = '<div class="no-bids">Esperando pujas...</div>'; return; }
            const sortedBids = [...bids].sort((a, b) => b.amount - a.amount);
            bidsContainer.innerHTML = sortedBids.map((bid, index) => {
                const timeStr = bid.timestamp.toLocaleTimeString();
                const isWinning = index === 0 ? ' winning' : '';
                return `<div class="bid-item${isWinning}">${index === 0 ? '👑 ' : ''}<span class="bid-user">${bid.username}</span><div class="bid-amount">${bid.amount} Pesetas</div><div class="bid-time">${timeStr}</div></div>`;
            }).join('');
        }

        function startAuction(id) {
            Object.keys(activeAuctions).forEach(key => { if (activeAuctions[key].active) activeAuctions[key].active = false; });
            const auction = activeAuctions[id];
            auction.active = true; 
            auction.timeLeft = 300; 
            auction.currentBid = auctionItems.find(item => item.id === id).startPrice; 
            auction.currentWinner = null; 
            auction.bidCount = 0;
            allBids[id] = [];
            addChatLog(`🚀 Subasta iniciada: ${auctionItems.find(i => i.id === id).title}`, 'success');
            renderAuctions(); 
            renderBids(id);
            const timer = setInterval(() => { 
                if (!auction.active) { clearInterval(timer); return; } 
                auction.timeLeft--; 
                if (auction.timeLeft <= 0) { clearInterval(timer); endAuction(id); } 
                renderAuctions(); 
            }, 1000);
        }

        function stopAuction(id) { endAuction(id); }

        function endAuction(id) {
            const auction = activeAuctions[id];
            auction.active = false;
            const item = auctionItems.find(i => i.id === id);
            if (auction.currentWinner) { 
                addChatLog(`🎉 Subasta finalizada: ${item.title} - Ganador: ${auction.currentWinner} (${auction.currentBid} Pesetas)`, 'success'); 
                alert(`¡Subasta finalizada!\\n\\n${item.title}\\nGanador: ${auction.currentWinner}\\nPrecio final: ${auction.currentBid} Pesetas`); 
            } else { 
                addChatLog(`⚠️ Subasta finalizada sin pujas: ${item.title}`, 'info'); 
                alert(`Subasta finalizada sin pujas: ${item.title}`); 
            }
            renderAuctions();
        }

        renderAuctions(); 
        renderBids(null); 
        addChatLog('💡 Presiona "Conectar" para empezar', 'info');
    </script>
</body>
</html>'''

with open('subasta_twitch_pesetas.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("✅ Versión con Pesetas (Puntos del Canal) creada!")
print("\n💰 CAMBIOS APLICADOS:")
print("=" * 60)
print("✨ Todos los precios ahora se muestran en 'Pesetas'")
print("📝 Campo del formulario: 'Precio Inicial (Pesetas)'")
print("💬 Mensajes del chat actualizados con 'Pesetas'")
print("🏆 Alertas de ganador con 'Pesetas'")
print("📊 Panel de pujas mostrando 'Pesetas'")
print("\n" + "=" * 60)
print("\nEjemplo de uso: Los viewers escriben '!300' en el chat")
print("La app mostrará: '300 Pesetas'")
print("\n" + "=" * 60)
print("\n📋 Copia el código completo:")
print("=" * 60)
print(html_code)
