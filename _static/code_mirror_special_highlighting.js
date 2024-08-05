CodeMirror.defineMode("commentOverlay", function() {
    return {
        token: function(stream, state) {
            if (stream.match("# TODO")) {
                return "todo";
            } else if (stream.match("# FIKSMEG")) {
                return "fiksmeg";
            } else if (stream.match("# FIKS MEG")) {
                return "fiksmeg";
            } else if (stream.match("# NOTE")) {
                return "note";
            } else if (stream.match("# FYLL INN")) {
                return "fyllinn";
            }
            while (stream.next() != null && 
                !stream.match("# TODO", false) && 
                !stream.match("# FIKSMEG", false) && 
                !stream.match("# FIKS MEG", false) && 
                !stream.match("# NOTE", false) &&
                !stream.match("# FYLL INN", false)) {}
            return null;
        }
    };
});