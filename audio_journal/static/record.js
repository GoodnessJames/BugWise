// Variable to store the audio element
const audioPlayer = document.getElementById('audio_player');
let mediaRecorder, chunks = [], audioURL = '';
const controllerWrapper = document.getElementById('recording-controls');

// Ensure that the script is executed after the HTML content is loaded
document.addEventListener('DOMContentLoaded', function () {

    // Initialize mediaRecorder setup for audio
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({
            audio: true
        }).then(stream => {
            mediaRecorder = new MediaRecorder(stream);

            mediaRecorder.ondataavailable = (e) => {
                chunks.push(e.data);
            };

            mediaRecorder.onstop = () => {
                const blob = new Blob(chunks, { 'type': 'audio/ogg; codecs=opus' });
                chunks = [];
                audioURL = window.URL.createObjectURL(blob);
                document.getElementById('audio_player').src = audioURL;
                document.getElementById('audio_data').value = audioURL;
                // Update the audio player source
                audioPlayer.src = audioURL;
            };
        }).catch(error => {
            console.log('Following error has occurred: ', error);
        });
    } else {
        console.log('MediaDevices not supported.');
    }

    // Start recording
    window.startRecording = function () {
        mediaRecorder.start();
        addMessage('Recording...');
    };

    // Stop recording
    window.stopRecording = function () {
        mediaRecorder.stop();
        addMessage('Recording stopped');
    };
    const addMessage = (text) => {
        const msg = document.createElement('p');
        msg.textContent = text;
        // Make the message disappear after 2 seconds
        controllerWrapper.appendChild(msg);
        setTimeout(() => {
            msg.remove();
        }, 2000);
    };
});