document.addEventListener("DOMContentLoaded", () => {
  const chatWindow = document.getElementById("chatWindow");
  const userInput = document.getElementById("userInput");
  const sendButton = document.getElementById("sendButton");

  const appendMessage = (message, sender) => {
    // 메시지가 비어 있으면 추가하지 않음
    if (!message) return;
    const messageBubble = document.createElement("div");
    // Add classes to the message bubble
    messageBubble.classList.add(
      "p-2",
      "rounded-lg",
      "max-w-xs",
      "break-words",
      "text-white"
    );
    if (sender === "user") {
      messageBubble.classList.add("bg-blue-500", "self-end");
    } else {
      messageBubble.classList.add("bg-gray-500", "self-start");
    }

    messageBubble.textContent = message;

    const messageWrapper = document.createElement("div");
    messageWrapper.classList.add(
      "flex",
      sender === "user" ? "justify-end" : "justify-start"
    );
    messageWrapper.appendChild(messageBubble);

    chatWindow.appendChild(messageWrapper);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  };

  const getBotResponse = (userMessage) => {
    // Simple responses for demonstration
    if (userMessage.toLowerCase().includes("hello")) {
      return "Hi there! How can I help you?";
    }
    return "I'm just a simple bot. Try saying 'hello'!";
  };

  const handleSendMessage = () => {
    const userMessage = userInput.value.trim();
    // 사용자 입력 메시지를 확인
    console.log("User Message:", userMessage);
    if (userMessage === "") return;

    // Clear the input box before appending the message
    userInput.value = ""; // 문제를 예방하기 위해 메시지 추가 전에 초기화

    // Display user's message
    appendMessage(userMessage, "user");

    // Get bot's response
    const botResponse = getBotResponse(userMessage);

    // 봇의 응답을 확인
    console.log("Bot Response:", botResponse);

    // Display bot's response after a short delay
    setTimeout(() => {
      appendMessage(botResponse, "bot");
    }, 500);

    // Clear input
    userInput.value = "";
  };

  sendButton.addEventListener("click", handleSendMessage);
  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handleSendMessage();
    }
  });
});
