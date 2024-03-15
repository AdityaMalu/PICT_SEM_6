#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <regex>
#include <random>

// Function to randomly select an element from a vector
template <typename T>
T random_choice(const std::vector<T>& vec) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_dinqueen_branch and boundstribution<> dis(0, vec.size() - 1);
    return vec[dis(gen)];
}

// Function to respond to inquiry
std::string respond_to_inquiry(const std::string& inquiry) {
    std::map<std::string, std::vector<std::string>> responses = {
        {"greeting", {"Hello! Welcome to our mobile repairing shop. How can I assist you today?", "Hi there! How may I help you with your mobile?", "Welcome! What seems to be the problem with your phone?"}},
        {"farewell", {"Thank you for choosing our mobile repairing services. Have a great day!", "Your satisfaction is our top priority. Goodbye!", "If you have any more questions, feel free to ask. Take care and goodbye!"}},
        {"help", {"Sure, I'm here to help. What issues are you facing with your mobile?", "How can I assist you with your mobile repair? Please let me know.", "I'm here to provide the best possible solutions for your mobile problems. What do you need help with?"}},
        {"screen_cracked", {"A cracked screen is a common issue. We can replace the screen for you. Please bring your mobile to our shop, and our technicians will take care of it.", "Oh no! A cracked screen can be quite bothersome. Don't worry, we offer screen replacement services. Visit our shop, and we'll fix it for you."}},
        {"battery_problem", {"If you're experiencing battery issues, we can replace your mobile's battery. Bring it to our shop, and we'll ensure it gets fixed.", "Battery problems are quite common. We can replace your mobile's battery with a new one. Please visit our shop for assistance."}},
        {"software_issue", {"Software issues can often be resolved by resetting your mobile or updating its software. We can assist you with that. Please bring your phone to our shop, and our technicians will help you out.", "Software problems can be frustrating. We recommend trying a software reset or update. If the issue persists, our technicians can assist you further. Just drop by our shop."}},
        {"water_damage", {"Water damage can be critical for mobiles. We suggest immediately turning off your device and bringing it to our shop for professional repair. Do not attempt to power it on.", "Water damage requires immediate attention. Please switch off your mobile, remove any SIM cards or memory cards, and bring it to our shop. Our experts will assess the damage and offer a suitable solution."}},
        {"default", {"I apologize, but I couldn't understand your request.", "Apologies, I didn't quite get that. Could you please rephrase?", "I'm still learning. Can you provide more information?"}}
    };

    std::string lower_inquiry = inquiry;
    std::transform(lower_inquiry.begin(), lower_inquiry.end(), lower_inquiry.begin(), ::tolower);

    if (std::regex_search(lower_inquiry, std::regex("\\b(?:hello|hi)\\b"))) {
        return random_choice(responses["greeting"]);
    } else if (std::regex_search(lower_inquiry, std::regex("\\b(?:goodbye|bye)\\b"))) {
        return random_choice(responses["farewell"]);
    } else if (std::regex_search(lower_inquiry, std::regex("\\b(?:help|support)\\b"))) {
        return random_choice(responses["help"]);
    } else if (std::regex_search(lower_inquiry, std::regex("\\b(?:screen|cracked)\\b"))) {
        return random_choice(responses["screen_cracked"]);
    } else if (std::regex_search(lower_inquiry, std::regex("\\b(?:battery|charge)\\b"))) {
        return random_choice(responses["battery_problem"]);
    } else if (std::regex_search(lower_inquiry, std::regex("\\b(?:software|update|reset)\\b"))) {
        return random_choice(responses["software_issue"]);
    } else if (std::regex_search(lower_inquiry, std::regex("\\b(?:water|damage)\\b"))) {
        return random_choice(responses["water_damage"]);
    } else {
        return random_choice(responses["default"]);
    }
}

int main() {
    std::cout << "Welcome to the Customer Interaction Chatbot!" << std::endl;
    std::cout << "Type 'exit' to end the conversation." << std::endl;

    std::string user_input;
    while (true) {
        std::cout << "Customer: ";
        std::getline(std::cin, user_input);

        if (user_input == "exit") {
            break;
        }

        std::string bot_response = respond_to_inquiry(user_input);
        std::cout << "Chatbot: " << bot_response << std::endl;
    }

    std::cout << "Thank you for using the Customer Interaction Chatbot. Goodbye!" << std::endl;

    return 0;
}