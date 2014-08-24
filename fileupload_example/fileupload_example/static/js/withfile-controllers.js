var WithFileControllers = angular.module('WithFileControllers', []);

WithFileControllers.controller('WithFileCtrl', ['$scope', '$dragon', '$upload', function($scope, $dragon, $upload) {
    $scope.withfile = {};
    $scope.progress = 0;

    $scope.updateProgress = function(progress, loaded, total) {
        $scope.progress = progress;
    };

    $scope.onFileSelect = function($files) {
        for (var i = 0; i < $files.length; i++) {
            var file = $files[i];
            $scope.upload = $upload.upload({
                url: window.swamp_dargon_host + '/_sdfileupload/',
                file: file
            }).progress(function(evt) {
                 $scope.progress = parseInt(100.0 * evt.loaded / evt.total);
            }).success(function(data, status, headers, config) {
                $scope.withfile.file = data.files[0];
            });
        }
    };

    $scope.save = function() {
        $scope.errors = null;
        $dragon.data.create('withfile-route', this.withfile).then(function(data) {
            console.log(data);
        }).catch(function(response) {
            $scope.errors = response.errors;
        })
    };
}]);


WithFileControllers.controller('MultiFileCtrl', ['$scope', '$dragon', '$upload', function($scope, $dragon, $upload) {
    $scope.multifile = {files: []};

    $scope.progress = 0;

    $scope.onFileSelect = function($files) {
        for (var i = 0; i < $files.length; i++) {
            var file = $files[i];
            $scope.upload = $upload.upload({
                url: window.swamp_dargon_host + '/_sdfileupload/',
                file: file
            }).progress(function(evt) {
                 $scope.progress = parseInt(100.0 * evt.loaded / evt.total);
            }).success(function(data, status, headers, config) {
                for (var i in data.files) {
                    $scope.multifile.files.push({file: data.files[i]});
                }
            });
        }
    };


    $scope.save = function() {
        var promise = null;
        $dragon.data.create('multifile-route', this.multifile).then(function(data) {
        }).catch(function(errors) {
            console.log(errors);
        })
    };
}]);


WithFileControllers.controller('WithFileListCtrl', ['$scope', '$dragon', function($scope, $dragon) {
    $scope.datasource = [];

    $dragon.data.onReady(function() {
        $dragon.data.getList('withfile-route').then(function(response) {
            $scope.datasource = response.data;
        }).catch(function(response) {
            console.log(response.errors);
        })
    });
}]);


WithFileControllers.controller('MultiFileListCtrl', ['$scope', '$dragon', function($scope, $dragon) {
    $scope.datasource = [];

    $dragon.data.onReady(function() {
        $dragon.data.getList('multifile-route').then(function(response) {
            $scope.datasource = response.data;
        }).catch(function(response) {
            console.log(response.errors);
        })
    });
}]);
