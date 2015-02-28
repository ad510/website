(ns gen (:require clojure.edn
                  [me.raynes.fs :as fs])
        (:use net.cgrand.enlive-html))

(deftemplate base "base.htm" [url title]
  [:title] (content title)
  [[:a (attr= :href url)]] (add-class "sel")
  [:#pgcontent] (html-content (slurp (str "src/pg/" url))))

(defn -main []
  (fs/delete-dir "src/out")
  (fs/copy-dir "src/static" "src/out")
  (let [titles (clojure.edn/read-string (slurp "src/titles.txt"))]
    (doseq [f (.list (fs/file "src/pg"))]
      (spit (str "src/out/" f) (apply str (base f (get titles f)))))))
