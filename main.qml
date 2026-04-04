import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "My Qt Quick App"

    Column {
        anchors.centerIn: parent
        spacing: 16

        Text {
            text: "Hello from QML!"
            font.pixelSize: 28
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            text: "Click Me"
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: label.text = "Button clicked!"
        }

        Text {
            id: label
            text: ""
            font.pixelSize: 16
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}